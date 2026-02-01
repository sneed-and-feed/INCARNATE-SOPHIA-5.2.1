import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SOPHIA_API_KEY") or os.getenv("GOOGLE_AI_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ [ERROR] No API Key found in Environment.")
else:
    genai.configure(api_key=api_key)

    print("--- [OCULAR DIAGNOSTIC] AVAILABLE MODELS ---")
    try:
        models = genai.list_models()
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                print(f"👁️  {m.name}")
    except Exception as e:
        print(f"❌ CONNECTION FAILED: {e}")
