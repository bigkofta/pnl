# 🎵 YouTube Downloader - Cursor Chat Commands

## 📋 Quick Copy/Paste Commands

### 🚀 Interactive Download
```bash
python cursor-downloader.py
```

### ⚙️ Check Current Settings
```bash
python cursor-downloader.py settings
```

### 📁 Change Format
```bash
# Switch to MP3
python cursor-downloader.py format mp3

# Switch to MP4 (video)
python cursor-downloader.py format mp4

# Switch to WAV
python cursor-downloader.py format wav
```

### 📂 Change Save Location
```bash
# Save to Desktop
python cursor-downloader.py directory ~/Desktop/YouTube

# Save to Downloads
python cursor-downloader.py directory ~/Downloads/YouTube

# Save to Music folder
python cursor-downloader.py directory ~/Music/YouTube
```

### ⚡ Quick Download Commands
```bash
# Basic download (auto-generated filename)
python cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00"

# Download with custom name
python cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00" "my_clip"

# Download as MP4 (one-time override)
python cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00" "my_clip" "mp4"

# Download as MP3 (one-time override)
python cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00" "my_clip" "mp3"
```

### 🎛️ Audio Tools (Post-Processing)
```bash
# Combine multiple files
python audio-tools.py combine file1.mp3 file2.mp3 combined.mp3

# Add fade effects (2s in, 3s out)
python audio-tools.py fade input.mp3 output.mp3 2 3

# Get file information
python audio-tools.py info filename.mp3

# Trim to specific section
python audio-tools.py trim input.mp3 output.mp3 "0:10" "0:45"

# Adjust volume (1.5x louder)
python audio-tools.py volume input.mp3 output.mp3 1.5
```

### 🛠️ Settings Management
```bash
# Open settings in Cursor
./manage-settings edit

# View all settings
./manage-settings show

# Quick format changes
./manage-settings mp3
./manage-settings mp4
./manage-settings wav

# Quick directory change
./manage-settings directory ~/Desktop/YouTube
```

## 💡 Template Commands (Fill in the blanks)

### Download Template
```bash
python cursor-downloader.py download "PASTE_YOUTUBE_URL_HERE" "START_TIME" "END_TIME" "OPTIONAL_NAME"
```

### Examples to Copy/Modify
```bash
# Example 1: Download 30-second MP3 clip
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "1:30" "2:00" "best_part"

# Example 2: Download 1-minute MP4 video segment
python cursor-downloader.py format mp4
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "2:15" "3:15" "video_clip"

# Example 3: Change to Desktop and download
python cursor-downloader.py directory ~/Desktop/YouTube
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "0:45" "1:30"
```

## 🎯 Workflow Examples

### Quick Audio Clip
1. Copy this command and modify the URL and times:
```bash
python cursor-downloader.py download "YOUR_URL_HERE" "START" "END" "clip_name"
```

### Change Format and Download
1. Set format:
```bash
python cursor-downloader.py format mp4
```
2. Download:
```bash
python cursor-downloader.py download "YOUR_URL_HERE" "START" "END"
```

### Multiple Segments
1. Download first segment:
```bash
python cursor-downloader.py download "URL" "1:00" "1:30" "intro"
```
2. Download second segment:
```bash
python cursor-downloader.py download "URL" "2:45" "3:15" "chorus"
```
3. Combine them:
```bash
python audio-tools.py combine intro.mp3 chorus.mp3 combined.mp3
```

## 🔧 Time Format Examples
All these formats work:
- `"90"` (90 seconds)
- `"1:30"` (1 minute 30 seconds)  
- `"0:01:30"` (1 minute 30 seconds)
- `"2:45"` (2 minutes 45 seconds)
- `"0:02:45"` (2 minutes 45 seconds) 