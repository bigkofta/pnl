#!/usr/bin/env python3
"""
Audio Tools - Combine, Split, and Edit MP3 files
Companion tool for YouTube Segment Downloader

Usage:
    python audio-tools.py combine file1.mp3 file2.mp3 [file3.mp3...] output.mp3
    python audio-tools.py split input.mp3 duration output_prefix
    python audio-tools.py fade input.mp3 output.mp3 [fade_in] [fade_out]
    python audio-tools.py trim input.mp3 output.mp3 start_time end_time
    python audio-tools.py volume input.mp3 output.mp3 volume_factor
    python audio-tools.py info file.mp3

Examples:
    # Combine multiple clips
    python audio-tools.py combine segment1.mp3 segment2.mp3 combined.mp3
    
    # Split a file into 30-second chunks
    python audio-tools.py split long_audio.mp3 30 chunk
    
    # Add fade in/out (2 seconds each)
    python audio-tools.py fade input.mp3 output.mp3 2 2
    
    # Trim to specific section
    python audio-tools.py trim input.mp3 output.mp3 "0:10" "0:45"
    
    # Adjust volume (2.0 = double, 0.5 = half)
    python audio-tools.py volume input.mp3 output.mp3 1.5
    
    # Get file info
    python audio-tools.py info segment1.mp3
"""

import sys
import subprocess
import os
import json
from pathlib import Path


def run_ffmpeg(cmd, description="Processing"):
    """Run FFmpeg command with error handling."""
    print(f"🎵 {description}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"FFmpeg error: {e.stderr}")
        return False


def parse_time_to_seconds(time_str):
    """Convert time string to seconds."""
    if ':' not in time_str:
        return float(time_str)
    
    parts = time_str.split(':')
    if len(parts) == 2:  # MM:SS
        return int(parts[0]) * 60 + float(parts[1])
    elif len(parts) == 3:  # HH:MM:SS
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    else:
        return float(time_str)


def get_audio_info(file_path):
    """Get detailed information about an audio file."""
    cmd = [
        'ffprobe', '-v', 'quiet', '-print_format', 'json',
        '-show_format', '-show_streams', file_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        # Extract relevant info
        format_info = data.get('format', {})
        stream_info = data.get('streams', [{}])[0]
        
        duration = float(format_info.get('duration', 0))
        bitrate = format_info.get('bit_rate', 'Unknown')
        sample_rate = stream_info.get('sample_rate', 'Unknown')
        channels = stream_info.get('channels', 'Unknown')
        
        return {
            'duration': duration,
            'bitrate': bitrate,
            'sample_rate': sample_rate,
            'channels': channels,
            'size': os.path.getsize(file_path)
        }
    except Exception as e:
        print(f"❌ Error getting file info: {e}")
        return None


def combine_audio_files(input_files, output_file):
    """Combine multiple audio files into one."""
    if len(input_files) < 2:
        print("❌ Error: Need at least 2 files to combine")
        return False
    
    # Check all input files exist
    for file in input_files:
        if not os.path.exists(file):
            print(f"❌ Error: File not found: {file}")
            return False
    
    # Create temporary file list for ffmpeg
    file_list = "file_list.txt"
    with open(file_list, 'w') as f:
        for file in input_files:
            f.write(f"file '{file}'\n")
    
    cmd = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', file_list,
        '-c', 'copy', '-y', output_file
    ]
    
    success = run_ffmpeg(cmd, f"Combining {len(input_files)} files")
    
    # Cleanup
    os.remove(file_list)
    
    if success:
        print(f"✅ Combined audio saved as: {output_file}")
        info = get_audio_info(output_file)
        if info:
            print(f"📁 Duration: {info['duration']:.1f}s, Size: {info['size']/(1024*1024):.1f}MB")
    
    return success


def split_audio_file(input_file, duration, output_prefix):
    """Split audio file into chunks of specified duration."""
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        return False
    
    cmd = [
        'ffmpeg', '-i', input_file, '-f', 'segment',
        '-segment_time', str(duration), '-c', 'copy',
        '-reset_timestamps', '1', '-y',
        f'{output_prefix}_%03d.mp3'
    ]
    
    success = run_ffmpeg(cmd, f"Splitting into {duration}s chunks")
    
    if success:
        # Count created files
        chunks = list(Path('.').glob(f'{output_prefix}_*.mp3'))
        print(f"✅ Created {len(chunks)} chunks:")
        for chunk in sorted(chunks):
            print(f"   📄 {chunk}")
    
    return success


def add_fade(input_file, output_file, fade_in=2, fade_out=2):
    """Add fade in/out effects to audio."""
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        return False
    
    # Get duration to calculate fade out start
    info = get_audio_info(input_file)
    if not info:
        return False
    
    duration = info['duration']
    fade_out_start = duration - fade_out
    
    cmd = [
        'ffmpeg', '-i', input_file,
        '-af', f'afade=t=in:ss=0:d={fade_in},afade=t=out:st={fade_out_start}:d={fade_out}',
        '-y', output_file
    ]
    
    success = run_ffmpeg(cmd, f"Adding fade in ({fade_in}s) and fade out ({fade_out}s)")
    
    if success:
        print(f"✅ Faded audio saved as: {output_file}")
    
    return success


def trim_audio(input_file, output_file, start_time, end_time):
    """Trim audio to specific time range."""
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        return False
    
    start_seconds = parse_time_to_seconds(start_time)
    end_seconds = parse_time_to_seconds(end_time)
    duration = end_seconds - start_seconds
    
    if duration <= 0:
        print("❌ Error: End time must be after start time")
        return False
    
    cmd = [
        'ffmpeg', '-i', input_file, '-ss', str(start_seconds),
        '-t', str(duration), '-c', 'copy', '-y', output_file
    ]
    
    success = run_ffmpeg(cmd, f"Trimming {start_time} to {end_time}")
    
    if success:
        print(f"✅ Trimmed audio saved as: {output_file}")
        print(f"📁 Duration: {duration:.1f}s")
    
    return success


def adjust_volume(input_file, output_file, volume_factor):
    """Adjust audio volume."""
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        return False
    
    cmd = [
        'ffmpeg', '-i', input_file,
        '-af', f'volume={volume_factor}',
        '-y', output_file
    ]
    
    success = run_ffmpeg(cmd, f"Adjusting volume by {volume_factor}x")
    
    if success:
        print(f"✅ Volume-adjusted audio saved as: {output_file}")
    
    return success


def show_info(input_file):
    """Display detailed information about an audio file."""
    if not os.path.exists(input_file):
        print(f"❌ Error: File not found: {input_file}")
        return False
    
    print(f"🎵 Audio File Information: {input_file}")
    print("=" * 50)
    
    info = get_audio_info(input_file)
    if not info:
        return False
    
    duration_min = info['duration'] // 60
    duration_sec = info['duration'] % 60
    size_mb = info['size'] / (1024 * 1024)
    
    print(f"📊 Duration: {duration_min:.0f}m {duration_sec:.1f}s ({info['duration']:.1f}s total)")
    print(f"📁 File Size: {size_mb:.1f} MB ({info['size']:,} bytes)")
    print(f"🎛️  Sample Rate: {info['sample_rate']} Hz")
    print(f"🔊 Channels: {info['channels']}")
    print(f"📡 Bitrate: {info['bitrate']} bps")
    
    return True


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'combine':
        if len(sys.argv) < 5:
            print("❌ Usage: combine file1.mp3 file2.mp3 [file3.mp3...] output.mp3")
            sys.exit(1)
        input_files = sys.argv[2:-1]
        output_file = sys.argv[-1]
        combine_audio_files(input_files, output_file)
    
    elif command == 'split':
        if len(sys.argv) != 5:
            print("❌ Usage: split input.mp3 duration output_prefix")
            sys.exit(1)
        input_file, duration, output_prefix = sys.argv[2:5]
        split_audio_file(input_file, float(duration), output_prefix)
    
    elif command == 'fade':
        if len(sys.argv) < 4:
            print("❌ Usage: fade input.mp3 output.mp3 [fade_in] [fade_out]")
            sys.exit(1)
        input_file, output_file = sys.argv[2:4]
        fade_in = float(sys.argv[4]) if len(sys.argv) > 4 else 2
        fade_out = float(sys.argv[5]) if len(sys.argv) > 5 else 2
        add_fade(input_file, output_file, fade_in, fade_out)
    
    elif command == 'trim':
        if len(sys.argv) != 6:
            print("❌ Usage: trim input.mp3 output.mp3 start_time end_time")
            sys.exit(1)
        input_file, output_file, start_time, end_time = sys.argv[2:6]
        trim_audio(input_file, output_file, start_time, end_time)
    
    elif command == 'volume':
        if len(sys.argv) != 5:
            print("❌ Usage: volume input.mp3 output.mp3 volume_factor")
            sys.exit(1)
        input_file, output_file, volume_factor = sys.argv[2:5]
        adjust_volume(input_file, output_file, float(volume_factor))
    
    elif command == 'info':
        if len(sys.argv) != 3:
            print("❌ Usage: info file.mp3")
            sys.exit(1)
        input_file = sys.argv[2]
        show_info(input_file)
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Available commands: combine, split, fade, trim, volume, info")
        sys.exit(1)


if __name__ == "__main__":
    main() 