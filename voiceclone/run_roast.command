#!/bin/bash
echo "🎤 STARTING PEP GUARDIOLA ROAST GENERATION..."
echo "💾 Using external drive for all storage"
echo ""

# Navigate to chatterbox directory
cd /Users/steve/chatterbox

# Activate conda environment
source /Users/steve/miniconda3/bin/activate chatterbox

# Run the voice cloner
python /Users/steve/SteveSystem/voiceclone/voice_cloner_external.py

echo ""
echo "🎉 Process complete! Check your external drive for the roast file."
read -p "Press Enter to close..." 