# Examples of histograms using trace function of kanga

# Restart the kernel before plotting each bivariate histogram

# %% Load packages

from numpy import genfromtxt

import kanga.plots as ps

# %% Read chains

chains = genfromtxt('chain01.csv', delimiter=',')

# %% Bivariate histogram of two parameters with default hist2d input arguments

ps.hist2d(chains[:, 1], chains[:, 2])

# %% Bivariate histogram of two parameters with custom number of bins

ps.hist2d(chains[:, 1], chains[:, 2], bins=30)

# %% Bivariate histogram of two parameters with various non-default input arguments

ps.hist2d(
    chains[:, 1],
    chains[:, 2],
    ranges=[[-8, 8], [-8, 8]],
    alpha=0.9,
    xlabel=r'Parameter $\theta_{}$'.format(1),
    ylabel=r'Parameter $\theta_{}$'.format(2),
    axes_labelsize=12,
    title=r'Bivariate histogram of parameters $(\theta_{},\theta_{})$'.format(1, 2),
    axes_titlesize=12,
    xtick_labelsize=10,
    ytick_labelsize=10
)

# %% Bivariate histogram of two parameters with color bar

ps.hist2d(
    chains[:, 1],
    chains[:, 2],
    ranges=[[-8, 8], [-8, 8]],
    density=True,
    alpha=0.9,
    xlabel=r'Parameter $\theta_{}$'.format(1),
    ylabel=r'Parameter $\theta_{}$'.format(2),
    axes_labelsize=12,
    title=r'Bivariate histogram of parameters $(\theta_{},\theta_{})$'.format(1, 2),
    axes_titlesize=12,
    xtick_labelsize=10,
    ytick_labelsize=10,
    cbar=True,
    cbar_labelsize=10
)
