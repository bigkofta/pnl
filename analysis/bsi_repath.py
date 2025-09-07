#!/usr/bin/env python3
"""
BSI Re-Pathing System
Detects low-conviction reads and guides user through targeted improvement prompts
"""

def calculate_bsi_score(analysis_data):
    """Calculate BSI score from analysis factors"""
    factors = analysis_data.get('intuitive_weighting', {}).get('strength_factors', {})
    
    symbolic_alignment = factors.get('symbolic_alignment', {}).get('score', 0)
    belief_intensity = factors.get('belief_intensity', {}).get('score', 0) 
    sentiment_intensity = factors.get('sentiment_intensity', {}).get('score', 0)
    narrative_breathability = factors.get('narrative_breathability', {}).get('score', 0)
    
    # Weighted BSI calculation (breathability is most important indicator)
    bsi_score = (
        symbolic_alignment * 0.2 +
        belief_intensity * 0.3 + 
        sentiment_intensity * 0.2 +
        narrative_breathability * 0.3
    )
    
    return bsi_score

def detect_low_flexibility_patterns(analysis_data, contra_flags):
    """Detect specific patterns indicating reduced mental flexibility"""
    patterns = []
    
    # Check for contradictory statements
    if len(contra_flags) > 2:
        patterns.append("high_contradiction_count")
    
    # Check for uneven cascade completion
    cascade_levels = analysis_data.get('in_game_cascade', {}).get('cascade_levels', [])
    if cascade_levels:
        completions = [level.get('completion', 0) for level in cascade_levels]
        if max(completions) - min(completions) > 40:  # High variance
            patterns.append("uneven_reasoning_chain")
    
    # Check for low narrative breathability
    breathability = analysis_data.get('intuitive_weighting', {}).get('strength_factors', {}).get('narrative_breathability', {}).get('score', 0)
    if breathability < 6.5:
        patterns.append("incomplete_narrative")
    
    # Check for binary thinking (extreme scores)
    factors = analysis_data.get('intuitive_weighting', {}).get('strength_factors', {})
    extreme_scores = 0
    for factor in factors.values():
        if isinstance(factor, dict) and 'score' in factor:
            score = factor['score']
            if score < 3 or score > 9:
                extreme_scores += 1
    
    if extreme_scores >= 2:
        patterns.append("binary_thinking")
    
    return patterns

def generate_repath_prompts(low_flexibility_patterns, original_read):
    """Generate targeted prompts based on detected patterns"""
    prompts = []
    
    if "high_contradiction_count" in low_flexibility_patterns:
        prompts.append({
            "type": "contradiction_resolution",
            "prompt": "I notice contradictory statements in your read. Let's clarify: You said [Player A] has X quality, but also said [Player B] can match it. Which is the dominant factor? Take 30 seconds to think through this one point only.",
            "focus": "logical_consistency"
        })
    
    if "uneven_reasoning_chain" in low_flexibility_patterns:
        prompts.append({
            "type": "reasoning_chain", 
            "prompt": "Your initial insight is strong, but the reasoning chain breaks down. Let's trace one path: IF your initial insight is correct, what would you expect to see happen first in the match? Just focus on the immediate next step.",
            "focus": "sequential_logic"
        })
    
    if "incomplete_narrative" in low_flexibility_patterns:
        prompts.append({
            "type": "narrative_expansion",
            "prompt": "The story feels incomplete. Imagine you're explaining this matchup to someone who's never seen either player. What's the ONE thing that makes this interesting? What's at stake beyond just winning?",
            "focus": "narrative_depth"
        })
    
    if "binary_thinking" in low_flexibility_patterns:
        prompts.append({
            "type": "nuance_injection",
            "prompt": "You're thinking in extremes (all power vs. no power). Let's add nuance: On a scale of 1-10, rate both players on the SAME dimension. Where do they actually differ by 2-3 points rather than 8-10 points?",
            "focus": "dimensional_thinking"
        })
    
    # Add reality anchor prompts based on Low BSI Reference Case learnings
    if any(pattern in low_flexibility_patterns for pattern in ["incomplete_narrative", "binary_thinking"]):
        prompts.append({
            "type": "eyes_never_lie_check",
            "prompt": "Stop analyzing and just observe: If you could see both players right now, what would their eyes tell you? What does their body language actually show? The eyes never lie - what do you SEE, not think?",
            "focus": "direct_observation"
        })
    
    if "high_contradiction_count" in low_flexibility_patterns or "binary_thinking" in low_flexibility_patterns:
        prompts.append({
            "type": "reality_anchor",
            "prompt": "You're building a theoretical framework. Step back: What actual evidence from recent matches, interviews, or head-to-head history supports this? What specific examples can you point to?",
            "focus": "evidence_grounding"
        })
    
    # Always include a state reset prompt
    prompts.append({
        "type": "state_reset",
        "prompt": "Take 60 seconds. Close your eyes. What's your gut feeling about this match when you're not trying to analyze it? What's the first image or word that comes to mind?",
        "focus": "intuitive_reset"
    })
    
    return prompts

def execute_repath_protocol(analysis_data, contra_flags, original_read):
    """Main re-pathing function"""
    bsi_score = calculate_bsi_score(analysis_data)
    
    print(f"🧠 BSI Score: {bsi_score:.1f}/10")
    
    if bsi_score < 7.0:  # Low BSI threshold
        print("🚨 LOW BSI DETECTED - Initiating Re-Path Protocol")
        
        patterns = detect_low_flexibility_patterns(analysis_data, contra_flags)
        prompts = generate_repath_prompts(patterns, original_read)
        
        print(f"\n🔍 Detected patterns: {', '.join(patterns)}")
        print(f"📋 Generated {len(prompts)} targeted prompts")
        
        # Priority order for prompts
        priority_order = ["state_reset", "contradiction_resolution", "narrative_expansion", "reasoning_chain", "nuance_injection"]
        
        sorted_prompts = []
        for priority in priority_order:
            for prompt in prompts:
                if prompt["type"] == priority:
                    sorted_prompts.append(prompt)
        
        return {
            "repath_required": True,
            "bsi_score": bsi_score,
            "patterns_detected": patterns,
            "prompts": sorted_prompts,
            "recommendation": "Complete at least the first 2 prompts before finalizing analysis"
        }
    else:
        return {
            "repath_required": False,
            "bsi_score": bsi_score,
            "status": "Analysis quality acceptable"
        }

# Example usage
if __name__ == "__main__":
    # Test with the Anisimova vs Sabalenka analysis
    test_analysis = {
        "intuitive_weighting": {
            "strength_factors": {
                "symbolic_alignment": {"score": 6.5},
                "belief_intensity": {"score": 7.2},
                "sentiment_intensity": {"score": 6.8},
                "narrative_breathability": {"score": 5.9}
            }
        },
        "in_game_cascade": {
            "cascade_levels": [
                {"completion": 75},
                {"completion": 45}, 
                {"completion": 60},
                {"completion": 30}
            ]
        }
    }
    
    test_contra_flags = [
        "Power assessment contradiction",
        "Mental state vs performance link unclear"
    ]
    
    result = execute_repath_protocol(test_analysis, test_contra_flags, "anisimova vs sabalenka read")
    
    print("\n" + "="*50)
    print("RE-PATH PROTOCOL RESULTS")
    print("="*50)
    print(f"BSI Score: {result['bsi_score']}")
    print(f"Re-path Required: {result['repath_required']}")
    
    if result['repath_required']:
        print(f"\nPatterns Detected: {result['patterns_detected']}")
        print(f"\nTargeted Prompts:")
        for i, prompt in enumerate(result['prompts'][:3], 1):
            print(f"\n{i}. {prompt['type'].upper()}")
            print(f"   Focus: {prompt['focus']}")
            print(f"   Prompt: {prompt['prompt']}") 