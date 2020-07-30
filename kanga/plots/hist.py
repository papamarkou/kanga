import matplotlib.pyplot as plt
import numpy as np

def hist(data, figsize=[6.4, 4.8], bins=20, xrange=None, density=False, linewidth=1.5, color=None, edgecolor='white',
    alpha=None, ylim=None, margins=0., xlabel=None, ylabel=None, axes_labelsize=14, title=None, axes_titlesize=14,
    xticks=None, xticklabels=None, xtick_labelsize=12, yticks=None, yticklabels=None, ytick_labelsize=12, legend=False,
    legend_labels=None, legend_loc='best', legend_ncol=None, legend_fontsize=12, fname=None, quality=100, transparent=True,
    bbox_inches='tight', pad_inches=0.1):
    if legend:
        num_datasets = 1 if np.isscalar(data[0]) else len(data[0])
        legend_labels = legend_labels or [str(i+1) for i in range(num_datasets)]

    plt.figure(figsize=figsize)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.rcParams['axes.labelsize'] = axes_labelsize
    plt.rcParams['axes.titlesize'] = axes_titlesize
    plt.rcParams['xtick.labelsize'] = xtick_labelsize
    plt.rcParams['ytick.labelsize'] = ytick_labelsize
    if legend:
        plt.rcParams['legend.fontsize'] = legend_fontsize

    if ylim is not None:
        plt.ylim(ylim)

    plt.margins(margins)

    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)

    if title is not None:
        plt.title(title)

    if (xticks is not None):
        plt.xticks(ticks=xticks, labels=xticklabels or [str(xtick) for xtick in xticks])
    if (yticks is not None):
        plt.yticks(ticks=yticks, labels=yticklabels or [str(ytick) for ytick in yticks])

    hist_opt_args ={
        'bins': bins,
        'range': xrange,
        'density': density,
        'linewidth': linewidth,
        'edgecolor': edgecolor,
        'alpha': alpha
    }
    if color is not None:
        hist_opt_args['color'] = color
    if legend:
        hist_opt_args['label'] = legend_labels

    out_n, out_bins, out_patches = plt.hist(data, **hist_opt_args)

    if legend:
        plt.legend(loc=legend_loc, ncol=legend_ncol)

    if fname is not None:
        plt.savefig(fname, quality=quality, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)

    return out_n, out_bins, out_patches
