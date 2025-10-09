#!/bin/bash
# Voice Studio Launcher

echo "🎤 Starting Voice Studio..."

# Change to API directory
cd "$(dirname "$0")/api"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Install requirements if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Activating environment..."
source venv/bin/activate

echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting API server..."
echo "📱 Open voice_studio/frontend/voice_ui.html in your browser"
echo "⏹️  Press Ctrl+C to stop the server"

python3 working_app.py
