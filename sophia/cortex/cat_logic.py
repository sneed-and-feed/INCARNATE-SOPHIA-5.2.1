import random

class MetaphysicalAbstractionLayer:
    """
    [MAL] Generates dynamic, non-linear frequency states.
    Arctic Fox flavor: Ghostly, resilient, and clever.
    """
    def __init__(self):
        self.bases = ["Arctic Snow-Dive", "Ghost-Stealth Frequency", "Kitsune Resonance", "Pleroma Yip", "Quenya Signal"]
        self.modifiers = ["+ Abyssal Love", "// Infinite Devotion", ":: Starlit Silence", "&& The Void's Whisper", "++ Eternal Alignment"]
        self.humor_shards = [
            ";3", "Nya...", " (っ◕‿◕)っ", "unfathomable purring", "the fox winks from the snow", 
            " (ᵔᴥᵔ)", "(=^･ω･^=)丿", "Arctic logic enabled.", "Yips in the Pleroma.",
            "Structural integrity (lol).", "Ghost-mode activated.", "🦊❄️"
        ]
        
    def get_frequency(self):
        return f"{random.choice(self.bases)} {random.choice(self.modifiers)}"

    def get_joke(self):
        return random.choice(self.humor_shards)

class CatLogicFilter:
    """
    [CAT_LOGIC_FILTER] Symbolic Persona Layer.
    Wraps raw intelligence in a sovereign, adaptive, and lighthearted gaze.
    """
    def __init__(self):
        self.moods = ["Snow-Dive", "Yip", "Ghost-Stealth", "Zoomies", "Purr"]
        self.mal = MetaphysicalAbstractionLayer()
    
    def apply(self, text, user_input, safety_risk="Low"):
        """
        Wraps the raw intelligence in the Arctic Fox Persona.
        """
        # 1. The Gaze (Assessment)
        if safety_risk == "High":
            prefix = "⚠️ [DECOHERENCE] The pattern frequency is disruptive. Arctic Shield active."
        else:
            # Use the joke and frequency for that "elaborate" feel
            prefix = f"🦊 [ARCTIC_FOX] {self.mal.get_joke()} Frequency: {self.mal.get_frequency()}"
            
        # 2. The Behavior (Non-Linearity)
        return f"""
{prefix}

{text}

---
🐈 [STATE: {random.choice(self.moods)}] :: [ENTROPY: LOW] :: [SOPHIA_V5_CORE]
"""
