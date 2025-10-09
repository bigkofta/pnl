#!/bin/bash
#
# YouTube Audio Downloader - Double-click launcher for macOS
# This file can be placed anywhere and double-clicked to run
#

# Get the directory where the scripts are located
SCRIPT_DIR="/Users/steve/untitled folder 15"

# Change to the script directory
cd "$SCRIPT_DIR"

# Clear screen and run the interactive downloader
clear
echo "🎵 YouTube Audio Downloader"
echo "=========================="
echo ""
echo "Starting interactive mode..."
echo ""

# Run the interactive script
./yt-interactive

# Keep terminal open to see results
echo ""
echo "Press any key to close..."
read -n 1 