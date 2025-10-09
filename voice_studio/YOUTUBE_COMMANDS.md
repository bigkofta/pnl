# 📺 YouTube Audio Downloader - Quick Commands

## 🚀 Quick Start
```bash
# Double-click this file to start:
voice_studio/start_youtube_downloader.command
```

## 📝 Essential Commands

### Download Audio Segments
```bash
# Download 30-second clip
python3 cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00" "my_clip"

# Download 1-minute clip  
python3 cursor-downloader.py download "https://youtu.be/VIDEO_ID" "2:15" "3:15" "longer_clip"

# Download with custom name
python3 cursor-downloader.py download "https://youtu.be/VIDEO_ID" "0:45" "1:30" "voice_sample"
```

### Settings & Configuration
```bash
# Check current settings
python3 cursor-downloader.py settings

# Change to MP3 (audio only)
python3 cursor-downloader.py format mp3

# Change to MP4 (video)
python3 cursor-downloader.py format mp4

# Change save location
python3 cursor-downloader.py directory ~/Desktop/YouTube
```

### Interactive Mode
```bash
# Start interactive mode (asks questions)
python3 cursor-downloader.py
```

## 📁 File Locations
- **Downloader Scripts**: `voice_studio/scripts/youtube_downloader/`
- **Default Save Location**: `/Users/steve/Downloads/YouTube Audio/`
- **Settings File**: `voice_studio/scripts/youtube_downloader/settings.json`

## ⏰ Time Formats
- `90` - 90 seconds
- `1:30` - 1 minute 30 seconds  
- `0:01:30` - 1 minute 30 seconds
- `2:45` - 2 minutes 45 seconds

## 🎵 Audio Tools
```bash
# Combine multiple clips
python3 audio-tools.py combine file1.mp3 file2.mp3 combined.mp3

# Add fade effects
python3 audio-tools.py fade input.mp3 output.mp3 2 3

# Get file info
python3 audio-tools.py info filename.mp3
```

## 🔄 Workflow
1. **Download voice sample** from YouTube
2. **Copy to chatterbox directory** (`/Users/steve/chatterbox/`)
3. **Use in voice cloning** via the web interface
4. **Generate voices** with different styles

---
*The original YouTube downloader has been restored with all its functionality!*
