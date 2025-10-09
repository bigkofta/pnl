# 🎵 YouTube Segment Downloader - Complete Guide

## 🚀 Quick Start

### Option 1: Double-Click (Easiest)
1. **Double-click** `YouTube Audio Downloader.command` on your Desktop
2. Follow the prompts to enter URL and timestamps
3. Choose MP3/MP4 and separate/combined options
4. Done! Files saved automatically

### Option 2: Terminal Command
```bash
# From anywhere in terminal
ytdl

# Or from this folder
./yt-interactive
```

## ⚙️ Settings & Configuration

### 🛠️ Edit Settings in Cursor
```bash
./manage-settings edit
```
This opens `settings.json` in Cursor where you can change:

- **Output Format**: `mp3`, `mp4`, `wav`
- **Save Location**: Any directory path
- **Quality**: Audio/video quality settings
- **File Naming**: Include timestamps, titles, etc.

### 📁 Quick Format Changes
```bash
./manage-settings mp3        # Switch to MP3
./manage-settings mp4        # Switch to MP4  
./manage-settings wav        # Switch to WAV
```

### 📂 Quick Directory Changes
```bash
./manage-settings directory ~/Desktop/YouTube
./manage-settings directory "/Users/steve/Music/Downloads"
```

### 📋 View Current Settings
```bash
./manage-settings show
```

## 🎯 Usage Examples

### Basic Download
```bash
ytdl
# Enter: https://youtu.be/VIDEO_ID
# Enter timestamps: 1:30 to 2:45
# Choose: Keep separate (1)
```

### Multiple Segments
```bash
ytdl
# Add segment 1: 0:30 to 1:00
# Add segment 2: 2:15 to 2:45  
# Add segment 3: 4:20 to 5:00
# Type 'done' when finished
# Choose: Combine all (2)
```

### Video Download (MP4)
```bash
./manage-settings mp4        # Switch to MP4 mode
ytdl                         # Run downloader
# Downloads video segments instead of audio
```

## 📁 File Locations

### Default Save Location
```
/Users/steve/Downloads/YouTube Audio/
```

### Current Settings File
```
/Users/steve/untitled folder 15/settings.json
```

### Scripts Location  
```
/Users/steve/untitled folder 15/
├── yt-interactive              # Main interactive script
├── manage-settings             # Settings manager
├── settings.json               # Configuration file
├── yt-segment.py              # Core downloader
├── audio-tools.py             # Audio editing tools
└── YouTube Audio Downloader.command  # Desktop launcher
```

## 🎛️ Advanced Features

### Audio Editing
After downloading, you can:

```bash
# Combine multiple files
python3 audio-tools.py combine file1.mp3 file2.mp3 output.mp3

# Add fade effects
python3 audio-tools.py fade input.mp3 output.mp3 2 3

# Trim to specific section
python3 audio-tools.py trim input.mp3 output.mp3 "0:10" "0:45"

# Adjust volume
python3 audio-tools.py volume input.mp3 output.mp3 1.5

# Get file info
python3 audio-tools.py info file.mp3
```

### Batch Processing
```bash
# Download multiple segments with custom names
ytdl
# Segment 1: 1:00-1:30 (name: "intro")
# Segment 2: 2:15-2:45 (name: "chorus") 
# Segment 3: 4:00-4:30 (name: "outro")
# Choose: Separate + Combined (3)
```

## 🔧 Settings Explained

### Output Formats
- **MP3**: Audio only, smallest files, most compatible
- **MP4**: Video + audio, larger files, full quality
- **WAV**: Uncompressed audio, largest files, highest quality

### Quality Settings
- **Audio Quality**: `best`, `good`, `medium`
- **Video Quality**: `720p`, `1080p`, `480p`

### File Naming Options
```json
{
  "file_naming": {
    "include_timestamp": true,    // Add time range to filename
    "include_title": true,        // Use video title in filename
    "sanitize_filenames": true    // Remove special characters
  }
}
```

## 🛠️ Troubleshooting

### Settings Not Loading
```bash
./manage-settings reset        # Reset to defaults
./manage-settings show         # Verify settings
```

### Downloads Failing
1. Check internet connection
2. Verify YouTube URL is valid
3. Try different video quality setting
4. Check if output directory is writable

### Opening in Cursor
If `./manage-settings edit` doesn't work:
1. Manually open: `/Users/steve/untitled folder 15/settings.json`
2. Edit in any text editor
3. Save changes

## 💡 Pro Tips

### Workflow Optimization
1. **Set your preferred format once**: `./manage-settings mp3`
2. **Set your preferred directory**: `./manage-settings directory ~/Desktop`
3. **Use the Desktop launcher** for quick access
4. **Bookmark frequently used video URLs**

### Time Format Flexibility
All these work:
- `90` (90 seconds)
- `1:30` (1 minute 30 seconds)
- `0:01:30` (1 minute 30 seconds)

### Keyboard Shortcuts
- **Ctrl+C**: Cancel download
- **Enter**: Use default options
- **Up Arrow**: Recall last command (in terminal)

## 🔄 Updating

To update settings after making changes:
1. Edit `settings.json` in Cursor
2. Save the file  
3. Next download will use new settings automatically

## 📞 Quick Reference

| Task | Command |
|------|---------|
| **Download segments** | `ytdl` or double-click launcher |
| **Edit settings** | `./manage-settings edit` |
| **Switch to MP4** | `./manage-settings mp4` |
| **Switch to MP3** | `./manage-settings mp3` |
| **Change directory** | `./manage-settings directory <path>` |
| **View settings** | `./manage-settings show` |
| **Reset everything** | `./manage-settings reset` | 