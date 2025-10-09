#!/usr/bin/env python3
"""
YouTube Downloader for Cursor IDE
Designed to be run from Cursor's integrated terminal or via chat commands
"""

import sys
import json
import subprocess
import os
from pathlib import Path
from config import load_settings, get_output_directory, get_download_command

def show_current_settings():
    """Display current settings in a nice format for Cursor chat."""
    settings = load_settings()
    print("🎵 YouTube Downloader - Current Settings")
    print("=" * 40)
    print(f"📁 Format: {settings['output_format'].upper()}")
    print(f"💾 Save to: {settings['output_directory']}")
    print(f"🎛️ Audio Quality: {settings['audio_quality']}")
    if settings['output_format'] == 'mp4':
        print(f"🎬 Video Quality: {settings['video_quality']}")
    print(f"📝 Include timestamps in filename: {settings['file_naming']['include_timestamp']}")
    print(f"🏷️ Include video title in filename: {settings['file_naming']['include_title']}")
    return settings

def quick_download(url, start_time, end_time, name=None, format_override=None):
    """Quick download function that can be called from Cursor chat."""
    print(f"🚀 Starting download...")
    print(f"📺 URL: {url}")
    print(f"⏰ Segment: {start_time} → {end_time}")
    
    # Load settings
    settings = load_settings()
    if format_override:
        settings['output_format'] = format_override
        print(f"🔄 Format override: {format_override.upper()}")
    
    output_dir = get_output_directory(settings)
    
    # Generate filename
    if not name:
        try:
            result = subprocess.run([
                'yt-dlp', '--get-title', url
            ], capture_output=True, text=True, check=True)
            title = result.stdout.strip()
            name = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            if settings["file_naming"]["include_timestamp"]:
                name = f"{name}_{start_time.replace(':', 'm')}-{end_time.replace(':', 'm')}"
        except:
            name = f"segment_{start_time.replace(':', 'm')}-{end_time.replace(':', 'm')}"
    
    # Build and run command
    cmd = get_download_command(settings, url, start_time, end_time, name, output_dir)
    
    print(f"📄 Output: {name}.{settings['output_format']}")
    print(f"📂 Location: {output_dir}")
    print()
    
    # Change to output directory and run
    original_dir = os.getcwd()
    try:
        os.chdir(output_dir)
        result = subprocess.run(cmd, check=True)
        
        # Check result
        format_ext = settings["output_format"]
        output_file = output_dir / f"{name}.{format_ext}"
        
        if output_file.exists():
            size_mb = output_file.stat().st_size / (1024 * 1024)
            print(f"\n✅ Success! Downloaded: {output_file.name}")
            print(f"📁 Size: {size_mb:.1f} MB")
            print(f"📂 Full path: {output_file}")
            return str(output_file)
        else:
            print("❌ Download completed but file not found")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Download failed: {e}")
        return None
    except KeyboardInterrupt:
        print("🛑 Download cancelled")
        return None
    finally:
        os.chdir(original_dir)

def set_format(format_type):
    """Change output format and save settings."""
    settings = load_settings()
    settings['output_format'] = format_type.lower()
    
    settings_file = Path(__file__).parent / "settings.json"
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=2)
    
    print(f"✅ Format changed to: {format_type.upper()}")
    return settings

def set_directory(directory_path):
    """Change output directory and save settings."""
    settings = load_settings()
    settings['output_directory'] = directory_path
    
    settings_file = Path(__file__).parent / "settings.json"
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=2)
    
    print(f"✅ Output directory changed to: {directory_path}")
    return settings

def interactive_mode():
    """Interactive mode for easy use in Cursor terminal."""
    print("🎵 YouTube Downloader - Cursor Integration")
    print("=" * 45)
    print()
    
    # Show current settings
    show_current_settings()
    print()
    
    # Get URL
    url = input("📺 YouTube URL: ").strip()
    if not url:
        print("❌ URL required")
        return
    
    print()
    print("⏰ Enter timestamps:")
    start_time = input("  Start time (MM:SS or HH:MM:SS): ").strip()
    end_time = input("  End time (MM:SS or HH:MM:SS): ").strip()
    
    if not start_time or not end_time:
        print("❌ Both start and end times required")
        return
    
    custom_name = input("  Custom filename (optional): ").strip()
    if not custom_name:
        custom_name = None
    
    print()
    format_choice = input("📁 Format override (mp3/mp4/wav, or Enter for current): ").strip()
    if not format_choice:
        format_choice = None
    
    print()
    return quick_download(url, start_time, end_time, custom_name, format_choice)

def main():
    """Main function with command line argument handling."""
    if len(sys.argv) == 1:
        # No arguments - run interactive mode
        interactive_mode()
    
    elif sys.argv[1] == "settings":
        show_current_settings()
    
    elif sys.argv[1] == "format":
        if len(sys.argv) != 3:
            print("Usage: python cursor-downloader.py format <mp3|mp4|wav>")
            return
        set_format(sys.argv[2])
    
    elif sys.argv[1] == "directory":
        if len(sys.argv) != 3:
            print("Usage: python cursor-downloader.py directory <path>")
            return
        set_directory(sys.argv[2])
    
    elif sys.argv[1] == "download":
        if len(sys.argv) < 5:
            print("Usage: python cursor-downloader.py download <url> <start> <end> [name] [format]")
            return
        
        url = sys.argv[2]
        start_time = sys.argv[3]
        end_time = sys.argv[4]
        name = sys.argv[5] if len(sys.argv) > 5 else None
        format_override = sys.argv[6] if len(sys.argv) > 6 else None
        
        quick_download(url, start_time, end_time, name, format_override)
    
    else:
        print("🎵 YouTube Downloader - Cursor Integration")
        print()
        print("Usage:")
        print("  python cursor-downloader.py                           # Interactive mode")
        print("  python cursor-downloader.py settings                  # Show current settings")
        print("  python cursor-downloader.py format <mp3|mp4|wav>      # Change format")
        print("  python cursor-downloader.py directory <path>          # Change output directory")
        print("  python cursor-downloader.py download <url> <start> <end> [name] [format]")
        print()
        print("Examples:")
        print("  python cursor-downloader.py")
        print("  python cursor-downloader.py format mp4")
        print("  python cursor-downloader.py directory ~/Desktop")
        print("  python cursor-downloader.py download 'https://youtu.be/VIDEO' '1:30' '2:00'")
        print("  python cursor-downloader.py download 'https://youtu.be/VIDEO' '1:30' '2:00' 'my_clip' 'mp4'")

if __name__ == "__main__":
    main() 