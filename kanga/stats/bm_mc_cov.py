import numpy as np

from kanga.emulators import optimal_ar_batch_size

from .bm_cov import bm_cov

def bm_mc_cov(x, b=None, r=3):
    if b is None:
        b = optimal_ar_batch_size(x)

    if ((r < 0) or (r > 5)):
        raise ValueError(' r={}. Pick a value of r in between 1 and 5'.format(r))

    if (b == 1 and r != 1):
        raise ValueError('r={} and b={}. If b=1, then r should be set to 1 too'.format(r, b))

    br = int(np.floor(b / r))
    if (br < 1):
        raise ValueError('floor(b/r)={}<1. Increase b or decrease r'.format(br))

    cov_mat = bm_cov(x, b)

    if (r > 1):
        # Lugsail lag window, see p. 4, eq. 2 in https://arxiv.org/pdf/1809.04541.pdf
        lug_cov_mat = 2 * cov_mat - bm_cov(x, br)

        if (lug_cov_mat.diagonal().prod() > 0):
            cov_mat = lug_cov_mat

    return cov_mat
