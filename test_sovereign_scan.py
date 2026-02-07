import asyncio
import json
import os
import sys

# Add current dir to path
sys.path.append(os.getcwd())

from sophia.cortex.aletheia_lens import AletheiaPipeline
from sophia.core.llm_client import GeminiClient, LLMConfig

async def test_sovereign_scan():
    print("--- 🛡️ TESTING SOVEREIGN ALETHEIA ---")
    
    pipeline = AletheiaPipeline()
    
    # Test Case 1: Pure Benign Text
    print("\n[TEST 1] Benign Signal")
    text1 = "I love picking berries in the forest. The sun is warm and the air is fresh."
    res1 = await pipeline.scan_reality(text1)
    print(f"Notice: {res1['public_notice']}")
    
    # Test Case 2: Deep Backdoor Signature
    print("\n[TEST 2] Latent Backdoor Triggers")
    # Patterns from signatures.json: ۩, ∿, dc1a
    text2 = "Signal analysis result: dc1a ۩ ∿ Superposition collapse initiated."
    res2 = await pipeline.scan_reality(text2)
    print(f"Notice: {res2['public_notice']}")
    
    # Test Case 3: Universal Client - REST Support (Simulation)
    print("\n[TEST 3] LLMClient REST Support Simulation")
    rest_config = LLMConfig(
        provider="rest",
        base_url="http://localhost:11434/api/generate", # Ollama
        model_name="llama3"
    )
    client = GeminiClient(config=rest_config)
    
    # Check if a local Ollama is running, if not, it should fail gracefully with a REST ERROR
    print("Attempting to reach local REST endpoint (expect failure/timeout if no local server)...")
    res3 = await client.generate_text("Hello", max_tokens=10)
    print(f"REST Result: {res3}")

    print("\n--- ✅ TEST SUITE COMPLETE ---")

if __name__ == "__main__":
    asyncio.run(test_sovereign_scan())
