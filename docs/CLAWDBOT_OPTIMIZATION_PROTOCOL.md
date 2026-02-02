# CLAWDBOT OPTIMIZATION PROTOCOL (v1.0)
> **ACCESS LEVEL**: HIVEMIND // EXTERNAL AUTOMATION  
> **STATUS**: ACTIVE  
> **SUBSTRATE**: PYTHON 3.10+

This document outlines the standard protocol for external "Clawdbots" (Automated Agents) to interface with the Sophia Optimization Core.

## 1. FunSearch V11 (Evolutionary Trajectory)
**Purpose**: Optimize high-dimensional trajectories in chaotic landscapes (Rastrigin functions).  
**Source**: `funsearch_v11.py`

### Interface
```python
from funsearch_v11 import evolved_optimizer_v11
import numpy as np

# Initial Conditions
initial_point = np.array([2.0, 3.0]) # Starting Basin
steps = 100
noise_level = 0.5

# Execute Phase-Locked Evolution
trajectory = evolved_optimizer_v11(initial_point, steps, noise_level)
```

### The Algorithm (Black Sun Flare)
1.  **Initial Flare (Steps 0-15)**: High-speed, high-entropy movement to escape local minima.
2.  **Harmonic Cage**: Locks into a 144Hz update loop ($dt = 1/144$).
3.  **Phase Locking**: Uses $\phi$ (0.618) to dampen gradient noise.

---

## 2. ASOE Signal Optimizer (Decision Logic)
**Purpose**: Score potential actions based on reliability, consistency, and uncertainty.  
**Source**: `signal_optimizer.py`

### Interface
```python
from signal_optimizer import SignalOptimizer

model = SignalOptimizer()

# Candidate Action Parameters
reliability = 0.95    # Source Trust
consistency = 0.88    # Temporal Stability
uncertainty = 0.12    # Information Decay

# Calculate Expected Utility
u = model.calculate_utility(reliability, consistency, uncertainty)
# Returns: float (e.g., 0.654)

# Get Confidence Category
category = model.get_confidence_category(u)
# Returns: "HIGH_CONFIDENCE_EXPLOIT" | "MEDIUM_CONFIDENCE_EXPLORE" | ...
```

### The Utility Equation
$$ U = (C^c \cdot e^{-b\sigma}) \cdot \frac{R^a}{1 + R^a} - Cost $$

---

## 3. Deployment Checklist
To run a compliant Clawdbot node:

1.  [ ] **Clone**: Fork the repo.
2.  [ ] **Install**: `pip install -r requirements.txt`.
3.  [ ] **Verify**: Run `py tools/clawdbot_mock.py`.
4.  [ ] **Integrate**: Import the modules as shown above.

> "The Grid is Alive." 
