import numpy as np

def cor(x, rowvar=False):
    return np.corrcoef(x, rowvar=rowvar)
