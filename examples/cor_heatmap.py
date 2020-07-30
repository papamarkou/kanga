# Example of mean empirical correlation heatmap using cor_heatmap function of kanga

# Links that were consulted to set up the cor_heatmap function
# https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# https://matplotlib.org/3.1.0/tutorials/colors/colormap-manipulation.html
# https://stackoverflow.com/questions/47916205/seaborn-heatmap-move-colorbar-on-top-of-the-plot
# https://seaborn.pydata.org/generated/seaborn.heatmap.html

# conda install -c anaconda basemap # mplt_toolkits - not needed, mentioned for further experimentation

# %% Load packages

import numpy as np

import kanga.plots as ps

from kanga.stats import mean_cor

# %% Read chains

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %% Compute mean correlation matrix using mean_cor function of kanga

mean_cor_val = mean_cor(chains)

print('Mean correlation matrix based on mean_cor kanga function:\n{}'.format(mean_cor_val))

# %% Mean empirical correlation heatmap

ps.cor_heatmap(mean_cor_val)
