import sys
import os
import numpy as np

# Ensure we can import from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from funsearch_v11 import evolved_optimizer_v11
    from signal_optimizer import SignalOptimizer
    from funsearch_harness import Evaluator
    print("[SUCCESS] Module Import Verified")
except ImportError as e:
    print(f"[FAILURE] Ingest Failed: {e}")
    sys.exit(1)

def run_clawdbot_cycle():
    print("\n--- CLAWDBOT OPTIMIZATION CYCLE ---")
    
    # 1. FUNSEARCH (Trajectory Optimization)
    print("[1] Executing FunSearch V11 (Black Sun Flare)...")
    evaluator = Evaluator()
    score, stats = evaluator.evaluate(evolved_optimizer_v11)
    print(f"    > Score: {score:.4f}")
    if score > 0.8:
        print("    > STATUS: OPTIMAL TRAJECTORY")
    else:
        print("    > STATUS: SUB-OPTIMAL")

    # 2. ASOE (Decision Scoring)
    print("\n[2] Executing ASOE (Signal Optimizer)...")
    model = SignalOptimizer()
    
    # Mock data stream
    candidates = [
        {'id': 'CMD_A', 'rel': 0.9, 'cons': 0.8, 'unc': 0.1},
        {'id': 'CMD_B', 'rel': 0.3, 'cons': -0.5, 'unc': 0.8}
    ]
    
    for c in candidates:
        u = model.calculate_utility(c['rel'], c['cons'], c['unc'])
        cat = model.get_confidence_category(u)
        print(f"    > {c['id']}: Utility={u:.3f} [{cat}]")
        
    print("\n[SUCCESS] Clawdbot Cycle Complete.")

if __name__ == "__main__":
    run_clawdbot_cycle()
