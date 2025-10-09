🎵 YOUTUBE SEGMENT DOWNLOADER
===============================

QUICK START:
============
1. Double-click "YouTube Audio Downloader.command" 
2. Paste YouTube URL when prompted
3. Enter start time (like 1:30)
4. Enter end time (like 2:00)
5. Choose separate files or combined
6. Done! Files saved automatically

WHERE ARE MY FILES SAVED?
=========================
Default location: /Users/steve/Downloads/YouTube Audio/
(Creates this folder automatically if it doesn't exist)

EASY COMMANDS FOR CURSOR:
=========================
Open Cursor terminal and copy/paste these:

# Download a segment
python cursor-downloader.py download "https://youtu.be/VIDEO_ID" "1:30" "2:00" "my_clip"

# Check current settings
python cursor-downloader.py settings

# Change to MP4 (video)
python cursor-downloader.py format mp4

# Change to MP3 (audio only)
python cursor-downloader.py format mp3

# Change save location
python cursor-downloader.py directory ~/Desktop/YouTube

# Interactive mode (asks questions)
python cursor-downloader.py

CHANGE SETTINGS:
===============
./manage-settings edit    (opens in Cursor)
./manage-settings mp4     (quick switch to MP4)
./manage-settings mp3     (quick switch to MP3)

TIME FORMATS THAT WORK:
======================
90          (90 seconds)
1:30        (1 minute 30 seconds)  
0:01:30     (1 minute 30 seconds)
2:45        (2 minutes 45 seconds)

AUDIO EDITING:
=============
# Combine multiple clips
python audio-tools.py combine file1.mp3 file2.mp3 combined.mp3

# Add fade effects
python audio-tools.py fade input.mp3 output.mp3 2 3

# Get file info
python audio-tools.py info filename.mp3

TROUBLESHOOTING:
===============
- If downloads fail: Check internet connection and YouTube URL
- If Cursor won't open settings: Manually open "settings.json" 
- If files not found: Check the save location in settings
- To reset everything: ./manage-settings reset

WHAT EACH FILE DOES:
===================
YouTube Audio Downloader.command  -> Double-click to start (main launcher)
cursor-downloader.py              -> For Cursor terminal commands
settings.json                     -> Configuration (edit in Cursor)
CURSOR_COMMANDS.md                -> Copy/paste commands for Cursor
HOW_TO_USE.md                     -> Detailed documentation
manage-settings                   -> Quick settings changes
audio-tools.py                   -> Audio editing features

EXAMPLES:
========
Download 30-second MP3:
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "1:30" "2:00"

Download 1-minute MP4:
python cursor-downloader.py format mp4
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "2:15" "3:15"

Save to Desktop:
python cursor-downloader.py directory ~/Desktop/YouTube
python cursor-downloader.py download "https://youtu.be/dQw4w9WgXcQ" "0:45" "1:30"

SUPPORT:
=======
All files are in: /Users/steve/untitled folder 15/
Settings file: settings.json (edit this to change format, save location, etc.)
Commands file: CURSOR_COMMANDS.md (copy/paste examples for Cursor)

That's it! Just double-click the launcher or use Cursor commands. 🎵 