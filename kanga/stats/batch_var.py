import numpy as np

from .batch_mean import batch_mean

def batch_var(x, b):
    return np.var(batch_mean(x, b), ddof=1)
