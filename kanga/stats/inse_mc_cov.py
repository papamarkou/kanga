# https://www.sciencedirect.com/science/article/pii/S0047259X16301877
# https://arxiv.org/pdf/1706.00853.pdf
# The notation follows the implementation of insec.cpp of the mcmcse R package

import numpy as np

from kanga.linalg import is_pos_def

def inse_mc_cov(x, adjust=False):
    x = x - x.mean(0)
    
    n, p = x.shape
    
    ub = int(np.floor(n / 2))
    sn = ub

    if adjust:
        Gamadj = np.zeros([p, p])

    for m in range(ub):
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

        if m == 0:
            Sig = -gam0 + 2 * Gam
        else:
            Sig = Sig + 2 * Gam

        if is_pos_def(Sig):
            sn = m
            break

    if sn > (ub-1):
        raise RuntimeError('Not enough samples')

    last_dtm = np.linalg.det(Sig)

    for m in range(sn + 1, ub):
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

        Sig1 = Sig + 2 * Gam

        current_dtm = np.linalg.det(Sig1)

        if current_dtm <= last_dtm:
            break

        Sig = Sig1.copy()

        last_dtm = current_dtm

        if adjust:
            eigenvals, eigenvecs = np.linalg.eig(Gam)
            eigenvals[eigenvals > 0] = 0
            Gamadj = Gamadj - eigenvecs @ np.diag(eigenvals) @ np.linalg.inv(eigenvecs)

    if adjust:
        Sig = Sig + 2 * Gamadj

    return Sig
