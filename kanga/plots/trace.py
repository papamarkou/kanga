import matplotlib.pyplot as plt
import numpy as np

from cycler import cycler

def trace(y, x=None, figsize=[8, 4], linewidth=None, color=None, ylim=None, margins=0., title=None, xlabel=None, ylabel=None,
    axes_labelsize=14, axes_titlesize=14, xticks=None, xticklabels=None, xtick_labelsize=12, yticks=None, yticklabels=None,
    ytick_labelsize=12, legend=False, legend_labels=None, legend_loc='best', legend_ncol=None, legend_fontsize=12,
    fname=None, quality=100, transparent=True, bbox_inches='tight', pad_inches=0.1):
    num_traces = 1 if np.isscalar(y[0]) else len(y[0])

    linewidth = linewidth or [1.5 for _ in range(num_traces)]
    color = color or ['#1f77b4' for _ in range(num_traces)]
    prop_cycle =  cycler(linewidth=linewidth) + cycler(color=color)

    if legend:
        legend_labels = legend_labels or [str(i+1) for i in range(num_traces)]

    plt.figure(figsize=figsize)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.gca().set_prop_cycle(prop_cycle)

    if ylim is not None:
        plt.ylim(ylim)

    plt.margins(margins)

    plt.rcParams['axes.labelsize'] = axes_labelsize
    plt.rcParams['axes.titlesize'] = axes_titlesize
    plt.rcParams['xtick.labelsize'] = xtick_labelsize
    plt.rcParams['ytick.labelsize'] = ytick_labelsize
    if legend:
        plt.rcParams['legend.fontsize'] = legend_fontsize

    if title is not None:
        plt.title(title)

    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)

    if (xticks is not None):
        plt.xticks(ticks=xticks, labels=xticklabels or [str(xtick) for xtick in xticks])
    if (yticks is not None):
        plt.yticks(ticks=yticks, labels=yticklabels or [str(ytick) for ytick in yticks])

    handles = plt.plot(x, y) if (x is not None) else plt.plot(y)

    if legend:
        plt.legend(handles=handles, labels=legend_labels, loc=legend_loc, ncol=legend_ncol)

    if fname is not None:
        plt.savefig(fname, quality=quality, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
