# 🎯 SteveSystem - Meta Content Orchestrator

A complete meta content orchestrator with master dashboard, voice cloning, analysis tools, and trading systems.

## 📁 Structure

```
ReflexBigChex/
├── index.html                    # 🎯 Master Dashboard
├── analysis/                     # 🧠 Analysis Tools
│   ├── contra.py                # Bias & contradiction detection
│   ├── bsi_repath.py            # Low-state recovery system
│   ├── validation_loop.py       # Reality-checking system
│   └── historical_cases/        # Validated precedent database
├── bsi scale/                   # 📊 BSI Analysis System
│   ├── unified_analysis_model.json
│   └── bsi.txt                  # Eyes Never Lie prompts
├── domains/                     # 🌍 Domain Analysis
│   └── soccer/                  # Football analysis
├── trading dashbaord/           # 📈 Trading Analysis
│   └── validation_report.json
├── voices/                      # 🎤 Voice Assets
│   ├── contra                   # Contra voices
│   └── skitz                    # Skitz voices
└── voice_studio/               # 🎵 Voice Cloning System
    ├── api/                    # FastAPI backend
    ├── frontend/               # Web interface
    └── scripts/                # Voice cloning + YouTube downloader
```

## 🚀 Quick Start

### 1. Master Dashboard
```bash
# Open the main dashboard
open index.html
```

### 2. Voice Cloning System
```bash
# Start voice studio
voice_studio/start_voice_studio.command

# Download YouTube samples (optional)
voice_studio/start_youtube_downloader.command

# Open voice interface
open voice_studio/frontend/voice_ui.html
```

### 3. Analysis Tools
```bash
# Contra analysis
python3 analysis/contra.py

# BSI re-path system
python3 analysis/bsi_repath.py

# Validation loop
python3 analysis/validation_loop.py
```

### 4. Trading Dashboard
```bash
# Open trading analysis
open "trading dashbaord/dashboard"
```

## 🎯 Features

### 🎤 Voice System
- **Multiple Voices**: Anisimova, Mel, Swiatek, Contra, Skitz
- **Multiple Styles**: Normal, Sassy, Roast, Calm, Hype, Confident
- **YouTube Download**: Extract voice samples with timestamps
- **Script Generation**: Built-in Pep Guardiola roast + custom text
- **Audio Tools**: Combine clips, add fades, get file info

### 🧠 Analysis Tools
- **Contra Analysis**: Automated bias and contradiction detection
- **BSI Re-Path System**: Low-state recovery with Eyes Never Lie prompts
- **Validation Loop**: Reality-checking against actual outcomes
- **Historical Cases**: Validated precedent database with learning

### 📊 Trading & Domains
- **Trading Dashboard**: Comprehensive analysis interface
- **Domain Analysis**: Soccer, basketball, and sports analysis
- **BSI Scale**: Unified analysis model with scoring

### 🎯 Master Dashboard
- **Unified Interface**: All components in one place
- **Workflow Integration**: GPT → Contra → BSI → Voices → Dashboard
- **Local Processing**: Everything runs on your machine

## 📖 Voice Cloning Guide

See `voice_studio/scripts/VOICE_CLONING_GUIDE.md` for detailed instructions on:
- Setting up the conda environment
- Downloading voice samples from YouTube
- Using different voice styles and parameters

## 🔧 Requirements

- Python 3.8+
- Conda environment with ChatterboxTTS
- Voice sample files (MP3/WAV)

## 📝 Usage

1. **Download voice samples** from YouTube using the scripts
2. **Start the API** server
3. **Open the web interface**
4. **Generate voices** with different styles
5. **Download audio files** for your projects

---

*Streamlined for maximum efficiency and ease of use.*