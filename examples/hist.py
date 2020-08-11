# Examples of histograms using hist function of kanga

# %% Load packages

from numpy import genfromtxt

import kanga.plots as ps

# %% Read chains

chains = genfromtxt('chain01.csv', delimiter=',')

num_iters, num_pars = chains.shape

# %% Histogram of a single chain with default hist input arguments

ps.hist(chains[:, 0])

# %% Histogram of a single chain with relative frequencies

ps.hist(chains[:, 0], density=True)

# %% Histogram of a single chain with some non-default hist input arguments

ps.hist(
    chains[:, 0],
    bins=25,
    xrange=[-10, 10],
    linewidth=2,
    density=True,
    edgecolor='black',
    title=r'Histogram of parameter $\theta_{{{}}}$'.format(1),
    xlabel='Parameter value',
    ylabel='Parameter relative frequency',
    axes_labelsize=18,
    axes_titlesize=20,
    xticks=[-10, -5, 0, 5, 10],
    xtick_labelsize=14,
    yticks = [0, 0.08, 0.16],
    ytick_labelsize=14
)

# %% Histograms of all three parameters

ps.hist(
    chains,
    color=['red', 'blue', 'green'],
    alpha=0.75,
    ylim=[0, 190],
    legend=True,
    legend_labels=[r'$\theta_{{{}}}$'.format(i+1) for i in range(num_pars)],
    legend_loc='upper left',
    legend_ncol=3,
    legend_fontsize=10,
)
