# Examples of running mean plots using running_mean function of kanga

# %% Load packages

import matplotlib.pyplot as plt

from numpy import genfromtxt
from statistics import mean

import kanga.plots as ps

# %% Read chains

chains = genfromtxt('chain01.csv', delimiter=',')

num_iters, num_pars = chains.shape

# %% Running mean plot of a single chain with default trace input arguments

ps.running_mean(chains[:, 0])

# %% Running mean plot of a single chain with a custom range of x values

ps.running_mean(chains[:, 0], x=range(1000, 1000 + num_iters))

# %% Running mean plot of a single chain with some non-default trace input arguments

ps.running_mean(
    chains[:, 0],
    ylim=[-2.7, 0.5],
    margins=0.01,
    title=r'Running mean plot of parameter $\theta_{{{}}}$'.format(1),
    xlabel='Iteration',
    ylabel='Running mean'
)

# %% Overlaid running mean plots of all three parameters
# Legend line width is set to be the same as line width in trace plot automatically

ps.running_mean(
    chains,
    linewidth=[1., 1.0, 1.0],
    color=['red', 'blue', 'green'],
    ylim=[-2.7, 0.5],
    legend=True,
    legend_labels=[r'$\theta_{{{}}}$'.format(i+1) for i in range(num_pars)],
    legend_loc='lower center',
    legend_ncol=num_pars,
    legend_fontsize=10
)

# %% Plot and show running mean without activating interactive mode to overlay a horizontal line to the plot
# See the following link:
# https://stackoverflow.com/questions/35492123/how-to-leave-matplotlib-figure-opened-after-script-ends

plt.ioff() # Use non-interactive mode
ps.running_mean(chains[:, 0], linewidth=[0.5], color=['blue'])
plt.hlines(mean(chains[:, 0]), 0, num_iters - 1, linewidth=2, color='red')
plt.show()
plt.ion()

# %% Plot and save running mean without activating interactive mode to overlay a horizontal line to the plot

# plt.ioff() # Use non-interactive mode
# ps.trace(chains[:, 0], linewidth=[0.5], color=['blue'])
# plt.hlines(mean(chains[:, 0]), 0, 1000, linewidth=2, color='red')
# plt.savefig('my_fig.pdf')
# plt.ion()
