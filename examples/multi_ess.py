# Compute multivariate ESS using multi_ess function based of kanga

# %% Load packages

import numpy as np

from kanga.stats import multi_ess

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

# %% Compute multivariate ESS using INSE MC covariance estimation

ess_val = multi_ess(chains)

print('Multivariate ESS using INSE MC covariance estimation: {}'.format(ess_val))

# %% Compute multivariate ESS using batch mean MC covariance estimation

ess_val = multi_ess(chains, method='bm')

print('Multivariate ESS using batch mean MC covariance estimation: {}'.format(ess_val))
