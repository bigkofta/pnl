#!/bin/bash
echo "🎯 STARTING PEP ROAST - NORMAL MODE (Better Pacing)"
echo "💾 Using external drive for all storage"
echo ""

# Navigate to chatterbox directory
cd /Users/steve/chatterbox

# Activate conda environment
source /Users/steve/miniconda3/bin/activate chatterbox

# Run the voice cloner with normal settings
python /Users/steve/SteveSystem/voiceclone/voice_cloner_external.py

echo ""
echo "🎉 Normal mode complete! Check your external drive for the new file."
read -p "Press Enter to close..." 