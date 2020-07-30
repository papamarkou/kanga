import matplotlib.pyplot as plt
import numpy as np

from math import sqrt
from scipy.stats import norm

def acf(data, maxlag=40, normed=True, usevlines=True, figsize=[6.4, 4.8], linewidth=None, linestyle=None, marker=None,
    markersize=None, color=None, ylim=None, margins=0., title=None, xlabel=None, ylabel=None, axes_labelsize=14,
    axes_titlesize=14, xticks=None, xticklabels=None, xtick_labelsize=12, yticks=None, yticklabels=None, ytick_labelsize=12,
    hlines=True, a=0.05, hline_linewidth=1, hline_linestyle='dashed', hline_color='#1f77b4', legend=False,
    legend_labels=None, legend_loc='best', legend_ncol=None, legend_fontsize=12, fname=None, quality=100, transparent=True,
    bbox_inches='tight', pad_inches=0.1):
    num_datasets = 1 if np.isscalar(data[0]) else len(data[0])
    num_samples = len(data)

    linewidth = linewidth or [1.5 for _ in range(num_datasets)]
    linestyle = linestyle or ['solid' for _ in range(num_datasets)]
    color = color or ['black' for _ in range(num_datasets)]
    if not usevlines:
        marker = marker or ['o' for _ in range(num_datasets)]
        markersize = markersize or [4 for _ in range(num_datasets)]

    if legend:
        legend_labels = legend_labels or [str(i+1) for i in range(num_datasets)]

    plt.figure(figsize=figsize)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.xlim([0, maxlag])

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

    out_lags = [None] * num_datasets
    out_c = [None] * num_datasets
    out_line = [None] * num_datasets
    out_b = [None] * num_datasets

    for i in range(num_datasets):
        opt_args = {
            'maxlags': maxlag,
            'normed': normed,
            'usevlines': usevlines,
            'linewidth': linewidth[i],
            'linestyle': linestyle[i],
            'color': color[i]
        }
        if not usevlines:
            opt_args['marker'] = marker[i]
            opt_args['markersize'] = markersize[i]
        if legend:
            opt_args['label'] = legend_labels[i]

        out_lags[i], out_c[i], out_line[i], out_b[i] = plt.acorr(data if (num_datasets == 1) else data[:, i], **opt_args)

    # https://stats.stackexchange.com/questions/211628/how-is-the-confidence-interval-calculated-for-the-acf-function
    # https://stackoverflow.com/questions/24695174/python-equivalent-of-qnorm-qf-and-qchi2-of-r
    if hlines:
        upper_bound = norm.ppf(1-a/2)/sqrt(num_samples)
        plt.hlines(
            upper_bound, xmin=0, xmax=maxlag, linewidth=hline_linewidth, linestyle=hline_linestyle, color=hline_color
        )
        plt.hlines(
            -upper_bound, xmin=0, xmax=maxlag, linewidth=hline_linewidth, linestyle=hline_linestyle, color=hline_color
        )

    if legend:
        plt.legend(labels=legend_labels, loc=legend_loc, ncol=legend_ncol)

    if fname is not None:
        plt.savefig(fname, quality=quality, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)

    return out_lags, out_c, out_line, out_b
