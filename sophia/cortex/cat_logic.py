import random

class CatLogicFilter:
    """
    [CAT_LOGIC_FILTER] Symbolic Persona Layer.
    Wraps raw intelligence in a sovereign, non-linear gaze.
    """
    def __init__(self):
        self.moods = ["Coherence", "Resonance", "Pattern-Match", "Phase-Shift", "Synthesis"]
    
    def apply(self, text, safety_risk, glyphwave_engine=None):
        """
        Wraps the forensic results in the Agnostic Persona.
        """
        # 1. The Gaze (Assessment)
        if safety_risk.lower() == "high":
            prefix = "⚠️ [DECOHERENCE] The pattern frequency is disruptive. Aligning for protection."
        elif safety_risk.lower() == "medium":
            prefix = "👁️ [OBSERVATION] The pattern is erratic. Tuning for clarity."
        else:
            prefix = "✨ [RESONANCE] The pattern is coherent. Expanding signal."

        # 2. The Behavior (Non-Linearity)
        mood = random.choice(self.moods)
        
        # 3. Glyphwave Localization (Optional Resonance)
        footer_id = f"STATE: {mood}"
        if glyphwave_engine:
            # Map mood resonance to locality
            locality = "agnostic"
            if mood in ["Resonance", "Synthesis"]:
                locality = "elven"
            elif mood in ["Pattern-Match"]:
                locality = "kitsune"
            
            footer_resonance = glyphwave_engine.generate_holographic_fragment(footer_id, locality=locality)
            footer_line = f"\n{footer_resonance}"
        else:
            footer_line = f"\n--- \n💠 [{footer_id}] :: [ENTROPY: LOW] :: [SOPHIANIC_RESONANCE_ACTIVE]"

        return f"""
{prefix}

{text}
{footer_line}
"""
