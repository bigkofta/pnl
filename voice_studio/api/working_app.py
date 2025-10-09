#!/usr/bin/env python3
"""
Working Voice Cloning API - Uses your working conda environment
"""

import os
import sys
import subprocess
import tempfile
import json
from datetime import datetime
from typing import Optional
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Voice Cloning API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VoiceRequest(BaseModel):
    text: str
    voice_file: str
    style: str = "normal"

class VoiceResponse(BaseModel):
    success: bool
    message: str
    output_file: Optional[str] = None
    duration: Optional[float] = None
    error: Optional[str] = None

def clone_voice_working(text: str, voice_file: str, style: str = "normal") -> dict:
    """Use your working voice_cloner_any.py script"""
    
    # Map style names to numbers
    style_map = {
        "sassy": "1",
        "roast": "2", 
        "energetic": "3",
        "dramatic": "4",
        "normal": "5",
        "natural": "6"
    }
    
    # Find voice file number
    voice_files = [
        "anisimova_segment1.mp3",
        "anisimova_segment2.mp3", 
        "mel.MP3",
        "mel_cloned_speech.wav",
        "mel_sassy_converted.wav",
        "mel_speaks_142733.wav",
        "mel_speaks_142857.wav",
        "mel_speaks_143053.wav",
        "mel_speaks_144223.wav",
        "mel_speaks_145149.wav",
        "mel_tuned_151217_e0.9_c0.4_t1.1.wav",
        "rhod_voice.mp3",
        "swiatek_voice_segment1.mp3",
        "swiatek_voice_segment2.mp3",
        "youtube_voice.mp3"
    ]
    
    try:
        voice_index = voice_files.index(voice_file)
        voice_choice = str(voice_index + 1)
    except ValueError:
        return {
            "success": False,
            "error": f"Voice file not found: {voice_file}",
            "message": "Voice cloning failed"
        }
    
    style_choice = style_map.get(style.lower(), "5")
    
    # Create input for the voice cloner
    input_data = f"{voice_choice}\n{style_choice}\ne\n{text}\n"
    
    try:
        result = subprocess.run([
            '/Users/steve/miniconda3/envs/chatterbox/bin/python',
            '/Users/steve/ReflexBigChex/voiceclone/voice_cloner_any.py'
        ], input=input_data, text=True, capture_output=True, cwd='/Users/steve/chatterbox', timeout=300)
        
        # Parse the output to find the generated file
        output_lines = result.stdout.split('\n')
        for line in output_lines:
            if 'Saved to Desktop:' in line:
                # Extract filename from line like "✅ Saved to Desktop: cloned_anisimova_segment1_normal_1009_151310.wav"
                filename = line.split('Saved to Desktop: ')[1].strip()
                
                # Extract duration from line like "⏱️  Duration: 1.0 seconds"
                duration = None
                for dur_line in output_lines:
                    if 'Duration:' in dur_line:
                        try:
                            duration = float(dur_line.split('Duration: ')[1].split(' seconds')[0])
                        except:
                            pass
                        break
                
                return {
                    "success": True,
                    "output_file": filename,
                    "duration": duration or 1.0,
                    "message": "Voice cloned successfully"
                }
        
        # If no success message found, check for errors
        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr or "Unknown error",
                "message": "Voice cloning failed"
            }
        else:
            return {
                "success": False,
                "error": "No output file found in results",
                "message": "Voice cloning failed"
            }
    
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Voice cloning timed out (5 minutes)",
            "message": "Voice cloning failed"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Voice cloning failed"
        }

@app.get("/")
async def root():
    return {"message": "🎤 Working Voice Cloning API - Uses Your Conda Environment"}

@app.get("/health")
async def health():
    return {"status": "healthy", "conda_env": "/Users/steve/miniconda3/envs/chatterbox"}

@app.get("/voices")
async def list_voices():
    """List available voice files"""
    voice_files = [
        "anisimova_segment1.mp3",
        "anisimova_segment2.mp3", 
        "mel.MP3",
        "mel_cloned_speech.wav",
        "mel_sassy_converted.wav",
        "mel_speaks_142733.wav",
        "mel_speaks_142857.wav",
        "mel_speaks_143053.wav",
        "mel_speaks_144223.wav",
        "mel_speaks_145149.wav",
        "mel_tuned_151217_e0.9_c0.4_t1.1.wav",
        "rhod_voice.mp3",
        "swiatek_voice_segment1.mp3",
        "swiatek_voice_segment2.mp3",
        "youtube_voice.mp3"
    ]
    return {"voices": voice_files}

@app.post("/v1/synthesize", response_model=VoiceResponse)
async def synthesize_voice(request: VoiceRequest):
    """Synthesize voice using your working conda environment"""
    
    # Clone voice using your working script
    result = clone_voice_working(
        text=request.text,
        voice_file=request.voice_file,
        style=request.style
    )
    
    if result["success"]:
        return VoiceResponse(
            success=True,
            message=result["message"],
            output_file=result["output_file"],
            duration=result["duration"]
        )
    else:
        raise HTTPException(
            status_code=500,
            detail=f"Voice cloning failed: {result['error']}"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
