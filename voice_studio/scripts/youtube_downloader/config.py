#!/usr/bin/env python3
"""
Configuration loader for YouTube Segment Downloader
Loads settings from settings.json file
"""

import json
import os
from pathlib import Path

def load_settings():
    """Load settings from settings.json file."""
    script_dir = Path(__file__).parent
    settings_file = script_dir / "settings.json"
    
    # Default settings if file doesn't exist
    default_settings = {
        "output_format": "mp3",
        "output_directory": str(Path.home() / "Downloads" / "YouTube Audio"),
        "audio_quality": "best",
        "video_quality": "720p",
        "auto_create_directory": True,
        "default_fade_in": 0,
        "default_fade_out": 0,
        "combine_by_default": False,
        "file_naming": {
            "include_timestamp": True,
            "include_title": True,
            "sanitize_filenames": True
        },
        "advanced": {
            "concurrent_downloads": 1,
            "retry_attempts": 3,
            "temp_directory": "/tmp/yt-downloader"
        }
    }
    
    try:
        if settings_file.exists():
            with open(settings_file, 'r') as f:
                settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                for key, value in default_settings.items():
                    if key not in settings:
                        settings[key] = value
                    elif isinstance(value, dict) and isinstance(settings[key], dict):
                        for subkey, subvalue in value.items():
                            if subkey not in settings[key]:
                                settings[key][subkey] = subvalue
                return settings
        else:
            # Create default settings file
            with open(settings_file, 'w') as f:
                json.dump(default_settings, f, indent=2)
            return default_settings
    except Exception as e:
        print(f"⚠️ Warning: Could not load settings ({e}), using defaults")
        return default_settings

def get_output_directory(settings):
    """Get and create output directory if needed."""
    output_dir = Path(settings["output_directory"])
    
    if settings["auto_create_directory"] and not output_dir.exists():
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created output directory: {output_dir}")
        except Exception as e:
            print(f"⚠️ Warning: Could not create directory {output_dir}: {e}")
            print(f"📁 Using current directory instead")
            return Path.cwd()
    
    return output_dir

def get_download_command(settings, url, start_time, end_time, output_name, output_dir):
    """Build yt-dlp command based on settings."""
    output_path = output_dir / f"{output_name}.%(ext)s"
    
    if settings["output_format"].lower() == "mp4":
        # Download video with specific segment
        cmd = [
            'yt-dlp',
            '--format', f'best[height<={settings["video_quality"][:-1]}]',
            '--postprocessor-args', f'ffmpeg:-ss {start_time} -t {calculate_duration(start_time, end_time)}',
            '--output', str(output_path),
            url
        ]
    else:
        # Download audio only (mp3, wav, etc.)
        quality = "0" if settings["audio_quality"] == "best" else "5"
        duration = calculate_duration(start_time, end_time)
        
        cmd = [
            'yt-dlp',
            '--extract-audio',
            '--audio-format', settings["output_format"],
            '--audio-quality', quality,
            '--postprocessor-args', f'ffmpeg:-ss {start_time} -t {duration}',
            '--output', str(output_path),
            url
        ]
    
    return cmd

def calculate_duration(start_time, end_time):
    """Calculate duration between start and end times."""
    def parse_time(time_str):
        parts = time_str.split(':')
        if len(parts) == 1:
            return int(parts[0])
        elif len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        else:
            raise ValueError(f"Invalid time format: {time_str}")
    
    start_seconds = parse_time(start_time)
    end_seconds = parse_time(end_time)
    return end_seconds - start_seconds

def open_settings_in_cursor():
    """Open settings.json in Cursor editor."""
    script_dir = Path(__file__).parent
    settings_file = script_dir / "settings.json"
    
    try:
        # Try to open with Cursor
        os.system(f'cursor "{settings_file}"')
        return True
    except Exception:
        try:
            # Fallback to default editor
            os.system(f'open "{settings_file}"')
            return True
        except Exception:
            print(f"📝 Please manually open: {settings_file}")
            return False 