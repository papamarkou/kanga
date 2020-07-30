from kanga import stats

from .trace import trace

def running_mean(y, x=None, figsize=[8, 4], linewidth=None, color=None, ylim=None, margins=0., title=None, xlabel=None,
    ylabel=None, axes_labelsize=14, axes_titlesize=14, xticks=None, xticklabels=None, xtick_labelsize=12, yticks=None,
    yticklabels=None, ytick_labelsize=12, fname=None, legend=False, legend_labels=None, legend_loc='best', legend_ncol=None,
    legend_fontsize=12, quality=100, transparent=True, bbox_inches='tight', pad_inches=0.1):
    means = stats.running_mean(y)

    trace(means, x=x, figsize=figsize, linewidth=linewidth, color=color, ylim=ylim, margins=margins, title=title,
        xlabel=xlabel, ylabel=ylabel, axes_labelsize=axes_labelsize, axes_titlesize=axes_titlesize, xticks=xticks,
        xticklabels=xticklabels, xtick_labelsize=xtick_labelsize, yticks=yticks, yticklabels=yticklabels,
        ytick_labelsize=ytick_labelsize, fname=fname, legend=legend, legend_labels=legend_labels, legend_loc=legend_loc,
        legend_ncol=legend_ncol, legend_fontsize=legend_fontsize, quality=quality, transparent=transparent,
        bbox_inches=bbox_inches, pad_inches=pad_inches
    )

    return means
