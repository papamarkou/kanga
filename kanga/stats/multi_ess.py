import numpy as np

from .bm_mc_cov import bm_mc_cov

def multi_ess(x, b=None, r=3):
    num_iters, num_pars = x.shape

    cov_mat_det = np.linalg.det(np.cov(x.transpose()))
    mc_cov_mat_det = np.linalg.det(bm_mc_cov(x, b=b, r=r))

    return num_iters * ((cov_mat_det / mc_cov_mat_det) ** (1/num_pars))
