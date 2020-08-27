# See lemma 2 of section 4.1 in https://www.tandfonline.com/doi/abs/10.1080/10618600.1998.10474787

import numpy as np

from kanga.linalg import is_pos_def, nearest_pd

from .mc_cov import mc_cov

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def multi_rhat(x, mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
    num_chains, num_iters, num_pars = x.shape

    w = np.zeros([num_pars, num_pars])
    for i in range(num_chains):
        if mc_cov_mat is None:
            w = w + mc_cov(x[i], method=method, adjust=adjust, b=b, r=r, rowvar=False)
        else:
            w = w + mc_cov_mat[i]
    w = w / num_chains

    if not is_pos_def(w):
        w = nearest_pd(w)
        is_w_pd = False
    else:
        is_w_pd = True

    b = np.cov(np.apply_along_axis(np.mean, 1, x), rowvar=False)

    if not is_pos_def(b):
        b = nearest_pd(b)
        is_b_pd = False
    else:
        is_b_pd = True

    rhat = np.max(np.linalg.eig(np.matmul(np.linalg.inv(w), b))[0])
    rhat = ((num_iters - 1) / num_iters) + ((num_chains + 1) / num_chains) * rhat

    return rhat, w, b, is_w_pd, is_b_pd
