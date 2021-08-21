import numpy as np

def cor_from_cov(x):
    num_pars = x.shape[1]
    sigma_inv = np.broadcast_to(1 / np.sqrt(np.diag(x)), (num_pars, num_pars))

    return x * sigma_inv * sigma_inv.transpose()
