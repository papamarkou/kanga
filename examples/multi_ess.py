# Compute univariate ESS using multi_ess function based of kanga

# %% Load packages

import numpy as np

# from kanga.stats import multi_ess

# mport statsmodels.api as sm
# from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.ar_model import ar_select_order
from statsmodels.tsa.stattools import acovf

# https://stats.stackexchange.com/questions/371792/sum-of-autocovariances-for-arp-model/372006#372006
# https://arxiv.org/pdf/1804.05975.pdf
# http://stat.wharton.upenn.edu/~steele/Courses/956/Resource/YWSourceFiles/WhyNotToUseYW.pdf
# https://ieeexplore.ieee.org/document/4547058

# %%

def approx_via_arp(x):
    n = len(x)

    ar_selection = ar_select_order(
        x,
        min(int(np.floor(n)), int(np.floor(10 * np.log10(n)))),
        ic='aic',
        trend='n',
        seasonal=False
    )

    ar_selection_order = ar_selection.ar_lags[-1]

    gammas = acovf(x, nlag=ar_selection_order-1, fft=False)

    model_fit = ar_selection.model.fit()
    
    param_sum = model_fit.params.sum()

    asympt_var = model_fit.sigma2 / ((1 - param_sum) ** 2)

    if (ar_selection_order != 0):
        Gamma = 0

        for i in range(1, ar_selection_order+1):
            for k in range(1, i+1):
                Gamma = Gamma + model_fit.params[i-1] * k * gammas[i-k]

        Gamma = 2 * (
            Gamma + 0.5 * (asympt_var - gammas[0]) * (model_fit.params * range(1, ar_selection_order + 1)).sum()
            ) / (1 - param_sum)
    else:
        Gamma = 0

    return Gamma, asympt_var

def optimal_batch_size(x):
    pass

# r = 1, 2, 3, 4 or 5
def mc_cov(x, r=3, batch_size=None, method='bm'):
    if batch_size is None:
        batch_size = optimal_batch_size(x, method=method)
    pass

def multi_ess(x):
    num_iters, num_pars = x.shape

    cov_mat = np.cov(x.transpose())

    cov_mat_det = np.linalg.det(cov_mat)
    mc_cov_mat_det = 1

    return num_iters * ((cov_mat_det / mc_cov_mat_det) ** (1/num_pars))

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

# %%

Gamma, asympt_var = approx_via_arp(chains[:, 0])

print(Gamma)
print(asympt_var)

# %%

from statsmodels.regression.linear_model import yule_walker

# %%

a1, b1 = yule_walker(chains[:, 0], order=2, method='mle')
print(a1)
print(b1**2)

# %%

from statsmodels.regression.linear_model import burg

# %%

a2, b2 = burg(chains[:, 0], order=2)
print(a2)
print(b2)

# %%

num_iters, num_pars = chains.shape

selection = ar_select_order(
    chains[:, 0],
    min(int(np.floor(num_iters)), int(np.floor(10 * np.log10(num_iters)))),
    ic='aic',
    trend='n',
    seasonal=False
)
print(selection.ar_lags)
res = selection.model.fit()
# print(res.summary())
print(res.params)
print(res.sigma2)

# %%

# %% Compute multivariate ESS

ess_val = multi_ess(chains)

print('Multivariate ESS: {}'.format(ess_val))
