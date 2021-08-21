# Examples of empirical correlation matrix computation using cor function

# %% Load packages

import numpy as np

from kanga.stats import cor

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

num_iters, num_pars = chains.shape

# %% Compute correlation matrix via numpy corrcoef function

np_cor_matrix = cor(chains)

print('Correlation matrix based on numpy corrcoef function:\n{}'.format(np_cor_matrix))
