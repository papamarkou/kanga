import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from .cmaps import redblue_cmap

def cor_heatmap(x, figsize=[7, 7], gridspec_kw=None, vmin=-1, vmax=1, cmap=redblue_cmap, linewidths=0.01,
    linecolor='white', cbar=True, cbar_kws=None, square=True, xticklabels=None, yticklabels=None, mask=None, upper=True,
    xtick_labelsize=8, ytick_rotation=0, ytick_labelsize=8, cbar_labelsize=8, fname=None, quality=100, transparent=True,
    bbox_inches='tight', pad_inches=0.1):
    num_params = x.shape[0]

    gridspec_kw = gridspec_kw or {'height_ratios': (0.93, .02), 'hspace': .03}

    cbar_kws = cbar_kws or {'orientation': 'horizontal'}
    xticklabels = xticklabels or range(1, num_params+1)
    yticklabels = yticklabels or range(1, num_params+1)
    if (mask is None) and upper:
        mask = np.tril(np.ones_like(x, dtype=np.bool))

    fig, (ax, cbar_ax) = plt.subplots(2, figsize=figsize, gridspec_kw=gridspec_kw)

    ax = sns.heatmap(
        x,
        vmin=vmin,
        vmax=vmax,
        cmap=cmap,
        linewidths=linewidths,
        linecolor=linecolor,
        cbar=cbar,
        cbar_kws=cbar_kws,
        cbar_ax=cbar_ax,
        square=square,
        xticklabels=xticklabels,
        yticklabels=yticklabels,
        mask=mask,
        ax=ax
    )
    
    ax.xaxis.tick_top()
    ax.yaxis.tick_right()

    ax.set_xticklabels(ax.get_xticklabels(), fontsize=xtick_labelsize)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=ytick_rotation, fontsize=ytick_labelsize)

    ax.collections[0].colorbar.ax.tick_params(labelsize=cbar_labelsize)

    if fname is not None:
        plt.savefig(fname, quality=quality, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)
