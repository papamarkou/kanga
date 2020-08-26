from .mc_cov import mc_cov
from .mc_se_from_cov import mc_se_from_cov

def mc_se(x, method='inse', adjust=False, b=None, r=3, rowvar=False):
    return mc_se_from_cov(mc_cov(x, method=method, adjust=adjust, b=b, r=r, rowvar=rowvar))
