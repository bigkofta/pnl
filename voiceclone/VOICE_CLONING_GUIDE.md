#!/usr/bin/env python3
"""
🎤 UNIVERSAL VOICE CLONER - FULL EXTERNAL DRIVE VERSION
Everything stored on external drive to save internal space!
"""

import os
import sys
import torch
import torchaudio as ta
import soundfile as sf
from datetime import datetime
import glob

# External drive configuration - EVERYTHING goes here
EXTERNAL_DRIVE = "/Volumes/$teve"
CHATTERBOX_DIR = "/Users/steve/chatterbox"
EXTERNAL_OUTPUT = f"{EXTERNAL_DRIVE}/voice_cloning_output"
EXTERNAL_TEMP = f"{EXTERNAL_DRIVE}/voice_cloning_temp"

def setup_external_storage():
    """Setup external drive directories for ALL voice cloning files"""
    directories = [
        f"{EXTERNAL_DRIVE}/torch_cache",
        f"{EXTERNAL_DRIVE}/huggingface_cache", 
        f"{EXTERNAL_DRIVE}/voice_cloning_temp",
        f"{EXTERNAL_DRIVE}/voice_cloning_output"
    ]
    
    print("🔧 Setting up external drive storage...")
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        print(f"📁 ✅ {dir_path}")
    
    # Set environment variables to use external drive for cache
    os.environ['TORCH_HOME'] = f"{EXTERNAL_DRIVE}/torch_cache"
    os.environ['HF_HOME'] = f"{EXTERNAL_DRIVE}/huggingface_cache"
    os.environ['TMPDIR'] = f"{EXTERNAL_DRIVE}/voice_cloning_temp"
    
    print(f"💾 All files will be stored on: {EXTERNAL_DRIVE}")
    print()

def find_audio_files():
    """Find all audio files in the current directory"""
    audio_extensions = ['*.mp3', '*.wav', '*.m4a', '*.flac', '*.ogg', '*.aac']
    audio_files = []
    
    for ext in audio_extensions:
        audio_files.extend(glob.glob(ext))
        audio_files.extend(glob.glob(ext.upper()))
    
    return sorted(audio_files)

def main():
    print("🎤 UNIVERSAL VOICE CLONER - FULL EXTERNAL MODE")
    print("=" * 55)
    print(f"💾 External drive: {EXTERNAL_DRIVE}")
    print("🎯 ALL files (cache + output) → External drive")
    print()
    
    # Setup external storage first
    setup_external_storage()
    
    # Change to chatterbox directory to find voice files
    os.chdir(CHATTERBOX_DIR)
    
    # The full Pep Guardiola roast script
    full_script = """did you guys see it pep guardiola the so-called bald genius the tactical messiah the cone collector in chief got cooked by frank the tank yeah first season in the prem for me i walk in like the substitute teacher with no lesson plan and i still schooled the so-called professor of football pep is old washed bald fraud ball more like fraud-ball tiki-taka now just ticki-tacky

they say man city hard to beat yeah we didn't even sign eze doesn't matter didn't need him because honestly playing city is like playing career mode on easy difficulty pep belongs back on football manager tapping spacebar not on my touchline watching me dance on his grave his team of oil princes couldn't even break down my danish ikea blueprint i beat him so easily it looked scripted

pep with all his millions all his lectures about half-spaces and positional play meanwhile i'm on the sideline in a coat looking like a viking substitute teacher and still running rings around him frank the tank never needed a transfer war chest just a brain heart and a little chaos the fact is city not scary anymore they're just old bald pep's powerpoint slides in motion

so go back to catalonia open up steam download football manager 2012 live in the past because the premier league is my classroom now and pep just failed the exam"""

    print("🎵 Searching for voice files...")
    audio_files = find_audio_files()
    
    if not audio_files:
        print("❌ No audio files found in the chatterbox directory!")
        print("💡 Add some audio files (.mp3, .wav, etc.) to /Users/steve/chatterbox/")
        input("Press Enter to exit...")
        return
    
    print("🎵 Available voice sources:")
    for i, file in enumerate(audio_files, 1):
        print(f"{i}. {file}")
    
    # Auto-select youtube_voice if available
    youtube_voice_idx = None
    for i, file in enumerate(audio_files):
        if "youtube_voice" in file.lower():
            youtube_voice_idx = i
            break
    
    if youtube_voice_idx is not None:
        reference_audio = audio_files[youtube_voice_idx]
        print(f"\n✅ Auto-selected: {reference_audio}")
    else:
        print("\n❌ youtube_voice.mp3 not found! Please select a voice:")
        try:
            choice = int(input(f"Select voice source (1-{len(audio_files)}): ")) - 1
            if choice < 0 or choice >= len(audio_files):
                raise ValueError()
            reference_audio = audio_files[choice]
        except (ValueError, IndexError):
            print("❌ Invalid choice!")
            input("Press Enter to exit...")
            return
    
    # Use ROAST MODE settings - perfect for the Pep script
    roast_settings = {
        "exaggeration": 0.5, 
        "cfg_weight": 0.5, 
        "temperature": 0.8, 
        "repetition_penalty": 1.0
    }
    
    print(f"\n🔥 ROAST MODE ACTIVATED!")
    print(f"🎵 Voice source: {reference_audio}")
    print(f"📝 Full Pep Guardiola roast script ({len(full_script)} characters)")
    print(f"💾 Model cache → {EXTERNAL_DRIVE}/torch_cache")
    print(f"📁 Output file → {EXTERNAL_OUTPUT}/")
    print(f"⚠️  Loading from external drive - may take 3-5 minutes...")
    print()
    
    try:
        print("🚀 Starting voice cloning process...")
        print("=" * 50)
        
        # Import and setup
        print("📦 Importing ChatterboxTTS...")
        from chatterbox.tts import ChatterboxTTS
        
        # Setup device
        if torch.backends.mps.is_available():
            device = "mps"
            print("🚀 Device: Apple Silicon GPU (MPS)")
        elif torch.cuda.is_available():
            device = "cuda"
            print("🚀 Device: NVIDIA GPU (CUDA)")
        else:
            device = "cpu"
            print("🖥️  Device: CPU (slower but stable)")
        
        print(f"⏳ Loading model to {device}...")
        print("📥 Downloading/loading from external cache...")
        
        # Load model - cache will be stored on external drive
        model = ChatterboxTTS.from_pretrained(device=device)
        print("✅ Model loaded successfully!")
        
        print(f"🎬 Generating speech with ROAST settings...")
        print(f"⏱️  Estimated time: 2-4 minutes for full script...")
        print("🔄 Processing...")
        
        # Generate the full script
        wav = model.generate(
            full_script,
            audio_prompt_path=reference_audio,
            **roast_settings
        )
        
        print("✅ Speech generation complete!")
        
        # Create output filename on external drive
        timestamp = datetime.now().strftime("%m%d_%H%M%S")
        voice_name = os.path.splitext(reference_audio)[0]
        output_file = f"pep_roast_{voice_name}_full_{timestamp}.wav"
        external_path = f"{EXTERNAL_OUTPUT}/{output_file}"
        
        print(f"💾 Saving to external drive...")
        # Save to external drive
        sf.write(external_path, wav.squeeze().numpy(), model.sr, subtype='PCM_16')
        
        # Calculate stats
        duration = wav.shape[-1] / model.sr
        file_size = os.path.getsize(external_path) / (1024 * 1024)
        
        print(f"\n🎉 ROAST MISSION ACCOMPLISHED!")
        print("=" * 50)
        print(f"✅ File saved: {output_file}")
        print(f"📁 Location: {external_path}")
        print(f"⏱️  Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
        print(f"📊 File size: {file_size:.1f} MB")
        print(f"💾 Everything stored on external drive")
        print(f"🔥 Pep Guardiola has been absolutely destroyed!")
        print()
        print(f"🎧 To play: Open Finder → {EXTERNAL_OUTPUT} → Double-click {output_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you're in the chatterbox conda environment")
        print("💡 Run: conda activate chatterbox")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

🚀 **RUNNING NOW - FULL EXTERNAL MODE!**

This will:
- 💾 **Cache files** → `/Volumes/$teve/torch_cache` 
- 📁 **Output file** → `/Volumes/$teve/voice_cloning_output/`
- 🎯 **Zero impact** on your internal drive space
- 🔥 **Full Pep roast script** in one generation

You'll see real-time progress showing model loading, generation progress, and final save location. The complete roasted Pep Guardiola rant will be ready in 3-5 minutes! 🎉 