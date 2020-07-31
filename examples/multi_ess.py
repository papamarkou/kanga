# Compute univariate ESS using multi_ess function based of kanga

# %% Load packages

import numpy as np

# from kanga.stats import multi_ess

# mport statsmodels.api as sm
# from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.ar_model import ar_select_order

# %%

def arp_approximation(x):
    n = len(x)

    ar_selection = ar_select_order(
        x,
        min(int(np.floor(n)), int(np.floor(10 * np.log10(n)))),
        ic='aic',
        trend='n',
        seasonal=False
    )

    model_fit = ar_selection.model.fit()
    asympt_var = model_fit.sigma2 / ((1 - model_fit.params.sum())**2)
    
    return asympt_var

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
print(res.summary())

# %%

# %% Compute multivariate ESS

ess_val = multi_ess(chains)

print('Multivariate ESS: {}'.format(ess_val))
