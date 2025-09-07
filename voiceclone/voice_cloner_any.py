#!/usr/bin/env python3
"""
🎤 UNIVERSAL VOICE CLONER
Clone ANY voice from ANY audio file!

Automatically saves all audio files to your Desktop.
"""

import os
import sys
import torch
import torchaudio as ta
import soundfile as sf
from datetime import datetime
import glob

# Make sure we're in the right directory
CHATTERBOX_DIR = "/Users/steve/chatterbox"
os.chdir(CHATTERBOX_DIR)

def find_audio_files():
    """Find all audio files in the current directory"""
    audio_extensions = ['*.mp3', '*.wav', '*.m4a', '*.flac', '*.ogg', '*.aac']
    audio_files = []
    
    for ext in audio_extensions:
        audio_files.extend(glob.glob(ext))
        audio_files.extend(glob.glob(ext.upper()))
    
    return sorted(audio_files)

def main():
    print("🎤 UNIVERSAL VOICE CLONER")
    print("=" * 50)
    print("Clone ANY voice from ANY audio file!")
    print()
    
    # Find available audio files
    audio_files = find_audio_files()
    
    if not audio_files:
        print("❌ No audio files found in the chatterbox directory!")
        print("💡 Add some audio files (.mp3, .wav, etc.) to /Users/steve/chatterbox/")
        input("Press Enter to exit...")
        return
    
    print("🎵 Available voice sources:")
    for i, file in enumerate(audio_files, 1):
        print(f"{i}. {file}")
    
    # Let user select voice source
    try:
        choice = int(input(f"\nSelect voice source (1-{len(audio_files)}): ")) - 1
        if choice < 0 or choice >= len(audio_files):
            raise ValueError()
        reference_audio = audio_files[choice]
    except (ValueError, IndexError):
        print("❌ Invalid choice!")
        input("Press Enter to exit...")
        return
    
    print(f"✅ Using voice from: {reference_audio}")
    
    # Voice style presets
    presets = {
        "1": {"name": "😤 SASSY", "settings": {"exaggeration": 0.9, "cfg_weight": 0.4, "temperature": 1.1, "repetition_penalty": 1.4}},
        "2": {"name": "🔥 ROAST MODE", "settings": {"exaggeration": 1.1, "cfg_weight": 0.35, "temperature": 1.2, "repetition_penalty": 1.3}},
        "3": {"name": "⚡ ENERGETIC", "settings": {"exaggeration": 0.8, "cfg_weight": 0.7, "temperature": 0.9}},
        "4": {"name": "🎭 DRAMATIC", "settings": {"exaggeration": 1.2, "cfg_weight": 0.3, "temperature": 1.0}},
        "5": {"name": "🎯 NORMAL", "settings": {"exaggeration": 0.5, "cfg_weight": 0.5, "temperature": 0.8}},
        "6": {"name": "🗣️ NATURAL", "settings": {"exaggeration": 0.4, "cfg_weight": 0.6, "temperature": 0.7}}
    }
    
    print("\n🎭 Choose voice style:")
    for key, preset in presets.items():
        print(f"{key}. {preset['name']}")
    
    style_choice = input("\nSelect style (1-6): ").strip()
    
    if style_choice not in presets:
        print("❌ Invalid choice!")
        input("Press Enter to exit...")
        return
    
    # Text options
    quick_texts = {
        "a": "Hello, this is a test of voice cloning technology. How does this sound?",
        "b": "I'm speaking with a cloned voice. This is pretty amazing technology!",
        "c": "You can make me say anything you want with this voice cloning system.",
        "d": "The future of AI voice synthesis is here, and it sounds incredible!",
        "e": "Custom text (type your own)"
    }
    
    print("\n📝 Quick text options:")
    for key, text in quick_texts.items():
        if key == "e":
            print(f"{key}. {text}")
        else:
            print(f"{key}. \"{text}\"")
    
    text_choice = input("\nSelect text (a-e): ").strip().lower()
    
    if text_choice in quick_texts:
        if text_choice == "e":
            text = input("📝 Enter your custom text: ").strip()
        else:
            text = quick_texts[text_choice]
    else:
        text = input("📝 Enter text to synthesize: ").strip()
    
    if not text:
        print("❌ No text entered!")
        input("Press Enter to exit...")
        return
    
    print(f"\n🎤 Generating {presets[style_choice]['name']} voice...")
    print(f"🎵 Voice source: {reference_audio}")
    print(f"📝 Text: {text}")
    
    try:
        # Import and setup
        from chatterbox.tts import ChatterboxTTS
        
        # Setup device
        if torch.cuda.is_available():
            device = "cuda"
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
        
        print(f"🔧 Using device: {device}")
        
        # Load model
        model = ChatterboxTTS.from_pretrained(device=device)
        
        # Generate with settings
        settings = presets[style_choice]['settings']
        wav = model.generate(
            text,
            audio_prompt_path=reference_audio,
            **settings
        )
        
        # Create filename based on source audio
        timestamp = datetime.now().strftime("%m%d_%H%M%S")
        style_name = presets[style_choice]['name'].replace('😤', '').replace('🔥', '').replace('⚡', '').replace('🎭', '').replace('🎯', '').replace('🗣️', '').strip()
        voice_name = os.path.splitext(reference_audio)[0]  # Remove extension
        output_file = f"cloned_{voice_name}_{style_name.lower().replace(' ', '_')}_{timestamp}.wav"
        
        # Save to Desktop in compatible format
        desktop_path = os.path.expanduser(f"~/Desktop/{output_file}")
        sf.write(desktop_path, wav.squeeze().numpy(), model.sr, subtype='PCM_16')
        
        duration = wav.shape[-1] / model.sr
        print(f"\n🎉 SUCCESS!")
        print(f"✅ Saved to Desktop: {output_file}")
        print(f"⏱️  Duration: {duration:.1f} seconds")
        print(f"📁 File location: {desktop_path}")
        print(f"💡 Double-click the file on your Desktop to play it!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you're in the chatterbox conda environment")
        print("💡 Run: conda activate chatterbox")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main() 