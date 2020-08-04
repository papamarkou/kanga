# Compute univariate ESS using multi_ess function based of kanga

# %% Load packages

import numpy as np

from kanga.stats import multi_ess

# %% Read chains

chains = np.genfromtxt('chain01.csv', delimiter=',')

# %% Compute multivariate ESS

ess_val = multi_ess(chains)

print('Multivariate ESS: {}'.format(ess_val))
