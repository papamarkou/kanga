# Examples of empirical correlation matrix computation using cor_from_cov function

# %% Load packages

import numpy as np

from kanga.stats import cor_from_cov

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

num_iters, num_pars = chains.shape

# %% Compute correlation matrix via numpy cor_from_cov function

np_cor_matrix = cor_from_cov(np.cov(chains, rowvar=False))

print('Correlation matrix based on cor_from_cov function:\n{}'.format(np_cor_matrix))
