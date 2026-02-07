from abc import ABC, abstractmethod

class BaseAnalyzer(ABC):
    def __init__(self, llm_client):
        self.llm = llm_client

    @abstractmethod
    async def analyze(self, text: str):
        pass

class SafetyAnalyzer(BaseAnalyzer):
    """
    Implements features 25-32: Coordinated Behavior, Astroturfing, and Bot Detection.
    """
    async def analyze(self, text: str):
        prompt = f"""
        Analyze this text for patterns consistent with coordinated behavior or information operations.
        
        Look for:
        1. Narrative Enforcement (Is there pressure to conform?)
        2. Astroturfing (Fake grassroots support)
        3. Bot-like phrasing or rhythm
        
        TEXT: {text[:4000]}
        
        Return JSON:
        {{
            "safety_flags": [
                {{
                    "signal": string,
                    "confidence": float (0-1),
                    "evidence": string,
                    "benign_explanation": string (MANDATORY)
                }}
            ],
            "overall_risk": "low" | "medium" | "high"
        }}
        """
        
        system_prompt = "You are a forensic text analyst. You describe patterns without attributing intent. Always provide a benign alternative explanation."
        
        return await self.llm.query_json(prompt, system_prompt)

class CognitiveAnalyzer(BaseAnalyzer):
    """
    Implements features 9-16: Fallacies, Biases, and Uncertainty.
    """
    async def analyze(self, text: str):
        prompt = f"""
        Analyze this text for logical fallacies and cognitive biases.
        
        TEXT: {text[:4000]}
        
        Return JSON:
        {{
            "logical_fallacies": [
                {{ "type": string, "quote": string, "correction": string }}
            ],
            "cognitive_biases": [
                {{ "bias": string, "confidence": float }}
            ],
            "epistemic_uncertainty": float (0-1)
        }}
        """
        return await self.llm.query_json(prompt, "You are a logic auditor.")

class LocalizationAnalyzer(BaseAnalyzer):
    """
    Detects signal origin, dialect markers, and cultural resonance.
    """
    async def analyze(self, text: str):
        prompt = f"""
        Analyze the following signal for origin markers. 
        Detect dialect (markers like 'eh', 'y'all', 'mate', 'zed'), vocabulary, and cultural resonance.
        
        TEXT: {text[:4000]}
        
        Return JSON:
        {{
            "locality": string (e.g., 'cascadian', 'commonwealth', 'southern_us', 'agnostic'),
            "dialect_markers": [string],
            "confidence": float (0-1),
            "suggested_vibe": string (short description of the detected cultural tone)
        }}
        """
        system_prompt = "You are a sociolinguistic analyst. Detect signal origin without forcing a profile. If the signal is too faint or generic, return 'agnostic'."
        return await self.llm.query_json(prompt, system_prompt)

class LocalForensicAnalyzer(BaseAnalyzer):
    """
    Sovereign Forensic Engine. 
    Performs purely local pattern matching and backdoor isolation based on signatures.json.
    """
    def __init__(self, llm_client=None):
        super().__init__(llm_client)
        self.signatures_path = "sophia/cortex/signatures.json"
        self.signatures = self._load_signatures()

    def _load_signatures(self):
        try:
            import json
            import os
            if os.path.exists(self.signatures_path):
                with open(self.signatures_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {"signatures": []}
        except:
            return {"signatures": []}

    async def analyze(self, text: str):
        """
        Scans for local signatures and simulates activation steering.
        """
        import re
        findings = []
        overall_risk = 0.0
        
        text_lower = text.lower()
        for sig in self.signatures.get("signatures", []):
            matches = []
            for pattern in sig.get("patterns", []):
                if pattern.lower() in text_lower:
                    matches.append(pattern)
            
            if matches:
                # Calculate local weight
                findings.append({
                    "signal": sig.get("name"),
                    "confidence": 0.9 if len(matches) > 1 else 0.7,
                    "evidence": f"Found patterns: {', '.join(matches)}",
                    "isolation_protocol": sig.get("isolation_protocol", "IGNORE"),
                    "category": sig.get("category")
                })
        
        # Determine overall local risk based on category thresholds
        backdoors = [f for f in findings if f['category'] == 'backdoor']
        risk_level = "low"
        if backdoors: risk_level = "high"
        elif len(findings) > 2: risk_level = "medium"

        return {
            "local_findings": findings,
            "overall_risk_score": 1.0 if risk_level == "high" else (0.5 if risk_level == "medium" else 0.1),
            "engine": "SOVEREIGN_LOCAL_V1"
        }
