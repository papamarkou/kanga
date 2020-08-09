from .bm_mc_cov import bm_mc_cov
from .inse_mc_cov import inse_mc_cov

def mc_cov(x, method='inse', adjust=False, b=None, r=3):
    if method == 'inse':
        return inse_mc_cov(x, adjust=adjust)
    elif method == 'bm':
        return bm_mc_cov(x, b=b, r=r)
    else:
        raise ValueError('The method can be inse or bm, {} was given'.format(method))
