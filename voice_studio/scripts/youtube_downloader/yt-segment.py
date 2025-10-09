#!/usr/bin/env python3
"""
YouTube Segment Downloader
Downloads specific time segments from YouTube videos as MP3 files.

Usage:
    python yt-segment.py <youtube_url> <start_time> <end_time> [output_name]

Examples:
    python yt-segment.py "https://youtu.be/dQw4w9WgXcQ" "0:30" "1:45"
    python yt-segment.py "https://youtu.be/dQw4w9WgXcQ" "1:20" "2:30" "my_clip"
    
Time formats supported: 
    - Seconds: 90
    - MM:SS: 1:30  
    - HH:MM:SS: 0:01:30
"""

import sys
import subprocess
import os
from pathlib import Path
from config import load_settings, get_output_directory, get_download_command


def parse_time(time_str):
    """Convert time string to seconds for ffmpeg."""
    parts = time_str.split(':')
    if len(parts) == 1:
        return int(parts[0])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    else:
        raise ValueError(f"Invalid time format: {time_str}")


def calculate_duration(start_time, end_time):
    """Calculate duration in seconds."""
    start_seconds = parse_time(start_time)
    end_seconds = parse_time(end_time)
    
    if end_seconds <= start_seconds:
        raise ValueError("End time must be after start time")
    
    return end_seconds - start_seconds


def download_segment(url, start_time, end_time, output_name=None):
    """Download a specific segment from YouTube video based on settings."""
    
    # Load settings
    settings = load_settings()
    output_dir = get_output_directory(settings)
    
    # Generate output filename if not provided
    if not output_name:
        # Get video title for filename
        try:
            result = subprocess.run([
                'yt-dlp', '--get-title', url
            ], capture_output=True, text=True, check=True)
            title = result.stdout.strip()
            # Clean filename
            output_name = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            if settings["file_naming"]["include_timestamp"]:
                output_name = f"{output_name}_{start_time.replace(':', 'm')}-{end_time.replace(':', 'm')}"
        except:
            output_name = f"segment_{start_time.replace(':', 'm')}-{end_time.replace(':', 'm')}"
    
    # Build command using settings
    cmd = get_download_command(settings, url, start_time, end_time, output_name, output_dir)
    
    # Determine expected output file
    format_ext = settings["output_format"] if settings["output_format"] != "mp4" else "mp4"
    output_file = output_dir / f"{output_name}.{format_ext}"
    
    print(f"🎵 Downloading segment {start_time} to {end_time} from: {url}")
    print(f"📁 Format: {settings['output_format'].upper()}")
    print(f"💾 Output directory: {output_dir}")
    print(f"📄 Output file: {output_file.name}")
    print(f"⚙️ Command: {' '.join(cmd)}")
    print()
    
    # Change to output directory for download
    original_dir = os.getcwd()
    try:
        os.chdir(output_dir)
        subprocess.run(cmd, check=True)
        print(f"\n✅ Successfully downloaded: {output_file.name}")
        
        # Check if file exists and show size
        if output_file.exists():
            size_mb = output_file.stat().st_size / (1024 * 1024)
            print(f"📁 File size: {size_mb:.1f} MB")
            print(f"📂 Location: {output_file}")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading segment: {e}")
        return False
    except KeyboardInterrupt:
        print(f"\n🛑 Download cancelled by user")
        return False
    finally:
        os.chdir(original_dir)
    
    return True


def main():
    """Main function to handle command line arguments."""
    
    if len(sys.argv) < 4:
        print(__doc__)
        print("\n❌ Error: Missing required arguments")
        print("Required: <youtube_url> <start_time> <end_time>")
        print("Optional: [output_name]")
        sys.exit(1)
    
    url = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]
    output_name = sys.argv[4] if len(sys.argv) > 4 else None
    
    # Validate time formats
    try:
        calculate_duration(start_time, end_time)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    # Validate URL (basic check)
    if not ('youtube.com' in url or 'youtu.be' in url):
        print("⚠️  Warning: URL doesn't appear to be a YouTube link")
    
    success = download_segment(url, start_time, end_time, output_name)
    
    if success:
        print("\n🎵 Segment download completed!")
    else:
        print("\n💥 Download failed!")
        sys.exit(1)


if __name__ == "__main__":
    main() 