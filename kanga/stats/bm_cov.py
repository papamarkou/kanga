import numpy as np

from .batch_mean import batch_mean

def bm_cov(x, b):
    col_batch_means = np.apply_along_axis(lambda v: batch_mean(v, b), 0, x)
    return b * np.cov(col_batch_means, rowvar=False)
