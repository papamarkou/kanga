# Compute potential scale reduction factor (Rhat) using rhat function of kanga, which is rhat of arviz

# %% Load packages

import numpy as np

from kanga.stats import uni_arviz_rhat

# %% Read chains

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %% Compute Rhat using rank method
# The output of rhat in kanga coincides with the output of Rhat in rstan
# See
# https://mc-stan.org/rstan/reference/Rhat.html

rhat_rank = uni_arviz_rhat(chains, method='rank')

print('rhat based on rank method: {}'.format(rhat_rank))
