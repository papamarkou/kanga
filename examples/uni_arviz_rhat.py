# Compute potential scale reduction factor (Rhat) using rhat function of kanga, which is rhat of arviz

# %% Load packages

import arviz as az
import numpy as np

# %% Define function for computing univariate Rhat based on arviz

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def uni_arviz_rhat(x, var_names=None, method='folded', vars=None):
    return [az.rhat(x.transpose()[i].transpose(), var_names=var_names, method=method) for i in vars or range(x.shape[2])]

# %% Read chains

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %% Compute Rhat using rank method
# The output of rhat in kanga coincides with the output of Rhat in rstan
# See
# https://mc-stan.org/rstan/reference/Rhat.html

rhat_rank = uni_arviz_rhat(chains, method='rank')

print('rhat based on rank method: {}'.format(rhat_rank))
