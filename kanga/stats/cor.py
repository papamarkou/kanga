import numpy as np

def cor(x):
    return np.corrcoef(x, rowvar=False)
