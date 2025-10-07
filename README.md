# 🎯 SteveSystem - Meta Content Orchestrator

## 🚀 **Quick Start - View Master Dashboard**

**Open `index.html` in your browser to see the complete system at a glance.**

The Master Dashboard shows:
- Real-time BSI monitoring
- Contra analysis results  
- Voice generation status
- Historical case references
- Trading dashboard integration
- All system components in one view

## Overview
The **SteveSystem** is a comprehensive automation toolkit that consolidates and orchestrates the entire trading content creation workflow. When you're not mentally "in it" but still need to produce quality reads, this system serves as your meta-orchestrator - bringing together analysis, bias checking, voice generation, and content delivery.

## 🎛️ **Master Dashboard Features**

### **📊 Live System Status**
- BSI Score monitoring with re-path alerts
- Contra analysis contradiction detection
- Soros alignment thermometer
- Component health indicators

### **🔄 Complete Workflow Integration**
- Read input and processing
- Automated bias checking
- Voice generation management
- Historical case referencing
- Trading dashboard access

### **🧠 Intelligence Components**
- **Contra Analysis**: Automated contradiction detection
- **BSI Re-Path**: Low-state recovery prompts
- **Skitz Voices**: Multiple perspective generation
- **Skincrawler**: Historical pattern matching
- **Example Weighting**: Precedent database

## 🔄 The Complete Workflow

### 1. **Content Creation** → GPT Chat
- Generate initial trading reads and analysis
- Raw content creation when mental state isn't optimal
- Extract key insights and market perspectives

### 2. **Content Consolidation** → Trading Dashboard
- Paste GPT-generated reads into the trading dashboard
- Centralize all analysis and market insights
- Track performance and accuracy over time

### 3. **Voice & Perspective Generation** → Skitz Integration
- Use different AI voices to present various perspectives
- Generate multiple viewpoints on the same trade/analysis
- Create engaging audio content from written reads

### 4. **Bias & Contradiction Checking** → Contra Analysis
- Automatically check reads for cognitive biases
- Identify logical contradictions in analysis
- Validate reasoning and assumptions
- Ensure balanced perspective before publication

### 5. **Meta Orchestration** → SteveSystem Core
- **BSI Scale Monitoring**: Track Behavioral State Index to adjust content strategy
- **Example Weighting**: Validate analysis with historical examples and precedents
- **User State Assessment**: Monitor mental/emotional state to adjust automation level
- **Quality Assurance**: Bring all components together for final content delivery

## 📁 System Architecture

```
SteveSystem/
├── index.html               # Master Dashboard (START HERE)
├── analysis/                # Core analysis engines
│   ├── contra.py           # Contradiction detection
│   ├── bsi_repath.py       # Low BSI recovery
│   ├── validation_loop.py  # Reality checking
│   └── historical_cases/   # Validated precedents
├── voiceclone/             # Voice generation tools
├── trading_dashboard/      # Analysis interface
├── bsi_scale/             # Behavioral monitoring
└── voices/                # Voice samples
```

## 🎯 The Meta-Orchestration Promise

**"Even when you're not mentally in it, the system ensures your content maintains the same quality, depth, and balanced perspective that your audience expects."**

This system consolidates:
- ✅ Content creation (GPT integration)
- ✅ Analysis and bias checking (Contra)
- ✅ Voice and perspective generation (Skitz/Voice cloning)
- ✅ Dashboard consolidation (Trading dashboard)
- ✅ State monitoring (BSI scale)
- ✅ Quality assurance (Meta orchestration)

## 🔧 Quick Setup

1. **View System**: Open `index.html` in browser
2. **Run Analysis**: Use `python analysis/contra.py` for bias checking
3. **Check BSI**: Use `python analysis/bsi_repath.py` for re-pathing
4. **Generate Voices**: Run voice cloning scripts in `voiceclone/`
5. **Access Dashboard**: Open `trading_dashboard/dashboard.html`

## 🎙️ Voice Cloning Tips (practical guidance)

These are light-weight suggestions based on what sounded best in recent runs. Use them as a guide, not hard rules.

- **What worked well**
  - Use a clean prompt: `anisimova_segment1.mp3` produced the most natural timbre.
  - Prefer NORMAL-ish settings: lower temperature/exaggeration/CFG keeps identity stable.
  - Generate in short chunks: shorter text preserves voice character and prosody.
  - Add punctuation and natural pauses to the script to guide cadence.

- **What to avoid (for long reads)**
  - One long generation in a single pass (identity/prosody drift over time).
  - Aggressive "sassy/roast" settings on long text (exaggerates drift/artifacts).
  - Noisy/expressive prompts for anchoring very long reads.

- **Simple recipe for long scripts**
  1) Anchor with the cleanest prompt (segment1).
  2) Keep settings conservative (NORMAL style, lower temperature/exaggeration).
  3) Split the script into 3–6 logical chunks with clear punctuation.
  4) Generate per chunk, then stitch the outputs.
  5) Normalize loudness if needed for consistency.

### Common artifacts: why they happen and how to fix

- **Elongated vowel / word loop (e.g., “wiiiiin”)**
  - Why: Over‑expressive params + under‑punctuated text cause prosody loops; long single‑pass increases drift.
  - Fix: Add commas/pauses; lower temperature/exaggeration; cfg_weight ≈ 0.55–0.60; raise repetition_penalty to 1.20–1.30; chunk long text.

- **Buzz/zip at phrase onset**
  - Why: Prompt→speech transition artifact or frame onset with very low energy.
  - Fix: Add a leading pause/comma or 100–200 ms silence; slightly raise cfg_weight; keep temperature modest.

- **Identity drift over long reads**
  - Why: Conditioning fades over time, amplified by spicy settings.
  - Fix: Use the cleanest prompt (seg1), NORMAL-ish settings, generate in chunks, stitch, normalize.

## 📚 Historical Learning

The system learns from validated cases:
- **Low BSI Reference Case**: Anisimova vs Sabalenka (Eyes Never Lie lesson)
- **Pattern Recognition**: Historical precedent matching
- **Continuous Improvement**: System updates based on real outcomes

## 🧠 Intelligence Layer

### **BSI Scale Integration**
- Monitors behavioral and emotional indicators
- Adjusts content automation based on mental state
- Ensures consistent quality regardless of personal condition

### **Bias Detection & Contradiction Analysis**
- **Contra System**: Automatically identifies logical inconsistencies
- **Perspective Weighting**: Balances bullish/bearish viewpoints
- **Historical Validation**: Cross-references with past market examples

### **User State Monitoring**
- Tracks engagement levels and decision-making capacity
- Adjusts automation vs manual control dynamically
- Maintains content quality standards consistently

---

*The SteveSystem: Your automated content creation safety net for when human intuition needs technological augmentation.* 