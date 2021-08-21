# Examples of autocorrelation plots using acf function of kanga

# %% Load packages

from numpy import genfromtxt

import kanga.plots as ps

# %% Read chains

chains = genfromtxt('chain01.csv', delimiter=',')

# %% ACF plot of a single chain with default acf input arguments

ps.acf(chains[:, 0])

# %% ACF plot of a single chain with y range [-1, 1]

ps.acf(chains[:, 0], ylim=[-1, 1])

# %% ACF plot of a single chain with some non-default acf input arguments

ps.acf(
    chains[:, 0],
    maxlag=50,
    usevlines=False,
    linewidth=[0.75],
    linestyle=['dotted'],
    marker='*',
    markersize=[4],
    color=['brown'],
    ylim=[-1, 1],
    hlines=True,
    hline_linewidth=0.75
)

# %% ACF plots of all three parameters

ps.acf(
    chains,
    maxlag=50,
    usevlines=False,
    linewidth=[1, 1, 1],
    linestyle=['solid', 'solid', 'solid'],
    marker=['.', '.', '.'],
    markersize=[2, 2, 2],
    color=['brown', 'blue', 'green'],
    ylim=[-1, 1],
    title='Autocorrelation plot',
    xlabel='Lag',
    ylabel='Autocorrelation',
    axes_labelsize=10,
    axes_titlesize=12,
    xticks=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
    xtick_labelsize=10,
    yticks=[-1, -0.5, 0, 0.5, 1],
    ytick_labelsize=10,
    hlines=True,
    hline_linewidth=0.75,
    legend=True,
    legend_ncol=3,
    legend_fontsize=10
)
