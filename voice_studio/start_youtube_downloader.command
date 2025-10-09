#!/bin/bash
# YouTube Downloader Launcher

echo "📺 Starting YouTube Audio Downloader..."

# Change to YouTube downloader directory
cd "$(dirname "$0")/scripts/youtube_downloader"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

echo "🚀 Starting YouTube downloader..."
echo "📱 Use the interactive mode or Cursor commands"
echo "⏹️  Press Ctrl+C to stop"

# Start the interactive downloader
python3 cursor-downloader.py
