# Examples of mean empirical correlation matrix computation using mean_cor function of kanga

# %% Load packages

import numpy as np

from kanga.stats import cor, mean_cor

# %% Read chains

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %% Compute mean correlation matrix using mean_cor function of kanga

mean_cor_val = mean_cor(chains)

print('Mean correlation matrix based on mean_cor kanga function:\n{}'.format(mean_cor_val))

# %% Compute empirical correlation matrix according to crosscorr function of coda, which merges multiple chains into one

coda_cor_val = cor(np.concatenate(chains))

print('Correlation matrix across chains computed according to coda crosscorr\n{}'.format(coda_cor_val))

# %% Difference between mean correlation matrix and correlation matrix computed according to coda crosscorr

cor_val_diff = mean_cor_val - coda_cor_val

print("Difference between mean correlation matrix and correlation matrix computed according to coda crosscorr:")
print(cor_val_diff)
