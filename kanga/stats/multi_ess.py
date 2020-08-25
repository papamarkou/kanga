import numpy as np

from .mc_cov import mc_cov

def multi_ess(x, cov_matrix=None, method='inse', adjust=False, b=None, r=3):
    num_iters, num_pars = x.shape

    cov_mat_det = np.linalg.det(np.cov(x, rowvar=False))
    mc_cov_mat_det = np.linalg.det(
        mc_cov(x, method=method, adjust=adjust, b=b, r=r, rowvar=False) if cov_matrix is None else cov_matrix
    )

    return num_iters * ((cov_mat_det / mc_cov_mat_det) ** (1/num_pars))
