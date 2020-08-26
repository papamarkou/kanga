import numpy as np

def mc_se_from_cov(x):
    return np.sqrt(np.diag(x))
