"""Generate a random number"""

# Imports ---------------------------------------------------------------------

import numpy as np

# Generate random number ------------------------------------------------------

def random_float() -> float:
    return float(np.random.rand(1)[0])