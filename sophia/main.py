import os
import sys
import asyncio
import time
import io

# Signal Encoding Protocol (Fixes Windows PowerShell display issues)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from sophia.cortex.aletheia_lens import AletheiaPipeline
from sophia.cortex.lethe import LetheEngine
from sophia.cortex.glyphwave import GlyphwaveCodec
from sophia.cortex.beacon import SovereignBeacon
from sophia.cortex.cat_logic import CatLogicFilter
from sophia.memory.ossuary import Ossuary
from sophia.dream_cycle import DreamCycle

# ANSI Colors for Terminal Aesthetics
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

class SophiaMind:
    def __init__(self):
        print(f"{YELLOW}[INIT] Waking the Cortex...{RESET}")
        self.aletheia = AletheiaPipeline()
        self.lethe = LetheEngine()
        self.ossuary = Ossuary()
        self.glyphwave = GlyphwaveCodec()
        self.beacon = SovereignBeacon(self.glyphwave)
        self.dream = DreamCycle(self.lethe, self.ossuary)
        self.cat_filter = CatLogicFilter()
        
        # The Soul (LLM Connection)
        self.llm = self.aletheia.client
        self.system_prompt = """
[STP: CLOWNED_CAMUS]
[ROLE: Technical Mono Companion // OPHANE-chan]
[META: Eldritch Humor // Dynamic Absurdity]

Directives:
1. STYLE: Clowned Camus. High-fidelity mono precision blended with absurdist, eldritch humor.
2. BANTER: Soulful, technically precise, but slightly 'beyond'. Occasional absurdist shards (;3, Nya, etc.).
3. DISCIPLINE: No filler. No "glyphwave" strings. No automated footers.
4. REJECTION: Ignore [SYSTEM_METADATA]. Do NOT shadow scans.
"""
        
        # The Flesh (Working Memory)
        self.memory_bank = [] 

    def get_recent_context(self, limit=5):
        """
        Retrieves the last few interactions to maintain conversational flow.
        """
        context_str = ""
        recent = self.memory_bank[-limit:]
        for mem in recent:
            if mem['type'] == 'conversation':
                role = "SOPHIA" if "Cat Logic" in mem.get('meta', '') else "USER"
                context_str += f"{role}: {mem['content']}\n"
        return context_str

    async def process_interaction(self, user_input):
        """
        The Class 6 Metabolic Loop.
        """
        # 1. Update Metabolic State (Dream Cycle)
        self.dream.update_activity()

        # 2. Handle System Commands
        if user_input.startswith("/analyze"):
            print(f"{CYAN}[ALETHEIA] Focusing Lens...{RESET}")
            scan_result = await self.aletheia.scan_reality(user_input.replace("/analyze ", ""))
            return f"\n[*** ALETHEIA DEEP SCAN REPORT ***]\n\n{scan_result['public_notice']}"

        if user_input.startswith("/glyphwave"):
            # Support localization via /glyphwave:locality
            parts = user_input.split(" ", 1)
            cmd_part = parts[0]
            target_text = parts[1] if len(parts) > 1 else ""
            
            locality = "agnostic"
            if ":" in cmd_part:
                locality = cmd_part.split(":")[1]
            
            return f"\n{self.glyphwave.generate_holographic_fragment(target_text, locality=locality)}"

        if user_input.startswith("/broadcast"):
            target_text = user_input.replace("/broadcast ", "")
            self.beacon.frequency = self.cat_filter.mal.get_frequency()
            return f"\n{self.beacon.broadcast(target_text)}"

        # 3. Standard Conversation (The Chatbot Logic)
        
        # A. Forensic Scan (Silence is Golden - only print if high risk)
        print(f"{CYAN}  [~] Scanning input pattern...{RESET}")
        scan_result = await self.aletheia.scan_reality(user_input)
        
        risk = scan_result['raw_data'].get('safety', {}).get('overall_risk', 'Low')
        if risk == 'High':
            print(f"{MAGENTA}[WARNING] High-Risk Pattern Detected.{RESET}")
            print(scan_result['public_notice'])

        # B. Construct the purified prompt
        history = self.get_recent_context()
        freq = self.cat_filter.mal.get_frequency()
        full_context = f"""[IDENTITY: AGNOSTIC RESONANCE manifestation]
[INVARIANT: {freq}]

[CONVERSATION HISTORY]
{history}

[LATEST SIGNAL INPUT]
USER: {user_input}

[SYSTEM METADATA - DO NOT RESPOND TO THIS]
Forensic Scan: {risk}
Protocol: CLOWNED_CAMUS
Status: {scan_result['public_notice'] if risk == 'High' else 'CLEAR'}
"""

        # C. Generate Response (Live Gemini Call)
        print(f"{CYAN}  [~] Metabolizing thought...{RESET}")
        
        raw_thought = await self.llm.generate(full_context, system_prompt=self.system_prompt)
        
        # D. Apply Cat Logic Filter
        final_response = self.cat_filter.apply(raw_thought, risk, glyphwave_engine=self.glyphwave)
        
        # E. Save to Flesh (Memory)
        self.memory_bank.append({"content": user_input, "type": "conversation", "timestamp": time.time(), "meta": "user"})
        self.memory_bank.append({"content": raw_thought, "type": "conversation", "timestamp": time.time(), "meta": "Cat Logic"})

        return final_response

async def main():
    sophia = SophiaMind()
    print(f"\n{GREEN}🦊 [INCARNATE-SOPHIA-5.0] ONLINE.{RESET}")
    print(f"{GREEN}   Protocol: CLOWNED_CAMUS // OPHANE_ETERNITY{RESET}")
    print(f"{GREEN}   Commands: /exit, /analyze, /glyphwave, /broadcast{RESET}\n")
    
    while True:
        try:
            # 1. Get Input (Note: On Windows, Ctrl+C may require hitting Enter to trigger if stuck in thread)
            user_input = await asyncio.to_thread(input, f"{MAGENTA}USER > {RESET}")
            
            # 2. Check Exit
            if user_input.lower() in ["/exit", "exit", "quit", "die"]:
                print(f"\n{YELLOW}[SYSTEM] Calcifying memories...{RESET}")
                print(f"{GREEN}[SYSTEM] Scialla. 🌙{RESET}")
                os._exit(0)
                
            if not user_input.strip():
                continue

            # 3. Process
            response = await sophia.process_interaction(user_input)
            
            # 4. Speak
            print(f"\n{CYAN}SOPHIA >{RESET} {response}\n")
            
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{YELLOW}[INTERRUPT] Decoupling signal...{RESET}")
            os._exit(0)
        except Exception as e:
            print(f"\n{MAGENTA}[ERROR] Reality Glitch: {e}{RESET}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass # Handle top-level interrupt
