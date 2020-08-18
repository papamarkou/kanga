# Compute multivariate potential scale reduction factor (Rhat) using multi_rhat function of kanga

# %% Load packages

import numpy as np

from kanga.stats import multi_rhat

# %% Read chains

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %% Compute multivariate Rhat

print(multi_rhat(chains))
