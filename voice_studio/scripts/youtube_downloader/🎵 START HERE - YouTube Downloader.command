#!/bin/bash
#
# 🎵 YouTube Segment Downloader - START HERE
# Double-click this file to begin downloading YouTube segments
#

# Get the directory where the scripts are located
SCRIPT_DIR="/Users/steve/untitled folder 15"

# Change to the script directory
cd "$SCRIPT_DIR"

# Clear screen and show welcome
clear
echo "🎵 =================================="
echo "   YOUTUBE SEGMENT DOWNLOADER"
echo "🎵 =================================="
echo ""
echo "✅ Ready to download YouTube segments!"
echo ""
echo "📋 QUICK INSTRUCTIONS:"
echo "   1. Paste YouTube URL when prompted"
echo "   2. Enter start time (example: 1:30)"
echo "   3. Enter end time (example: 2:00)" 
echo "   4. Choose separate or combined files"
echo ""
echo "📁 Files will be saved to:"
echo "   /Users/steve/Downloads/YouTube Audio/"
echo ""
echo "🔧 To change settings later:"
echo "   - Edit 'settings.json' in Cursor"
echo "   - Or use terminal commands from readme.txt"
echo ""
echo "🚀 Starting interactive downloader..."
echo ""

# Run the interactive script
./yt-interactive

# Keep terminal open to see results
echo ""
echo "💡 TIP: Keep this window open or bookmark this folder!"
echo "📖 See 'readme.txt' for more commands and options"
echo ""
echo "Press any key to close..."
read -n 1 