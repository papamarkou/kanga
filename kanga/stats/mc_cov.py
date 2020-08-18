import numpy as np

from .bm_mc_cov import bm_mc_cov
from .inse_mc_cov import inse_mc_cov

def mc_cov(x, method='inse', adjust=False, b=None, r=3):
    if method == 'inse':
        return inse_mc_cov(x, adjust=adjust)
    elif method == 'bm':
        return bm_mc_cov(x, b=b, r=r)
    elif method == 'iid':
        return np.cov(x, rowvar=False)
    else:
        raise ValueError('The method can be inse, bm or iid, {} was given'.format(method))
