import numpy as np

from kanga.emulators import approx_ar_cov_sum

def optimal_ar_batch_size(x):
    num_iters = x.shape[0]

    ar_approximation = np.apply_along_axis(approx_ar_cov_sum, 0, x) ** 2
    coeff = (ar_approximation[0, ].sum() / ar_approximation[1, ].sum()) ** (1 / 3)

    b = int(np.floor((num_iters ** (1 / 3)) * coeff))
    if b == 0:
        b = 1

    return b
