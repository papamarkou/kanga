import numpy as np

from .mc_cov import mc_cov

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def multi_rhat(x, method='inse', adjust=False, b=None, r=3):
    num_chains, num_iters, num_pars = x.shape

    w = np.zeros([num_pars, num_pars])
    for i in range(num_chains):
        w = w + mc_cov(x[i], method=method, adjust=adjust, b=b, r=r)
    w = w / num_chains

    b = np.cov(np.apply_along_axis(np.mean, 1, x), rowvar=False)

    v = ((num_iters - 1) / num_iters) * w + ((num_chains + 1) / (num_chains * num_iters)) * b

    rhat = max(np.linalg.eig(np.matmul(np.linalg.inv(w), v))[0])

    return rhat, v, w, b
