from .cor_from_cov import cor_from_cov
from .mc_cov import mc_cov

def mc_cor(x, method='inse', adjust=False, b=None, r=3, rowvar=False):
    return cor_from_cov(mc_cov(x, method=method, adjust=adjust, b=b, r=r, rowvar=rowvar))
