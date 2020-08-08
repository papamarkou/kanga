# See https://arxiv.org/pdf/1706.00853.pdf
# The notation follows the implementation of insec.cpp of the mcmcse R package

import numpy as np

def inse_mc_cov(x):
    x = x - x.mean(0)
    
    n, p = x.shape
    
    sn = int(np.floor(n / 2))
    
    for m in range(sn):
        gam0 = np.zeros([p, p])
        gam1 = np.zeros([p, p])

        for i in range(n - 2 * m):
            gam0 = gam0 + np.outer(x[i, :], x[i + 2 * m, :])
        gam0 = gam0 / n

        for i in range(n - 2 * m - 1):
            gam1 = gam1 + np.outer(x[i, :], x[i + 2 * m + 1, :])
        gam1 = gam1 / n
        
        Gam = gam0 + gam1
        Gam = (Gam + Gam.transpose()) / 2
        
        return Gam
