# Compute IMSE Monte Carlo covariance estimate using inse_mc_cov function based of kanga

# %% Load packages

import numpy as np

from kanga.stats import inse_mc_cov

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

# %% Compute IMSE Monte Carlo covariance estimate

inse_mc_cov_val = inse_mc_cov(chains)

print('INSE Monte Carlo covariance estimate:\n{}'.format(inse_mc_cov_val))

# %% Compute adjusted IMSE Monte Carlo covariance estimate

adj_inse_mc_cov_val = inse_mc_cov(chains, adjust=True)

print('Adjusted INSE Monte Carlo covariance estimate:\n{}'.format(adj_inse_mc_cov_val))
