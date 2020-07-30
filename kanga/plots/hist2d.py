import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

from .cmaps import redblue_cmap

def hist2d(x, y, figsize=[6.4, 4.8], bins=20, ranges=None, density=False,
    cmap=redblue_cmap, norm=mcolors.Normalize(), vmin=None, vmax=None, alpha=None, xlabel=None, ylabel=None,
    axes_labelsize=14, title=None, axes_titlesize=14, xticks=None, xticklabels=None, xtick_labelsize=12, yticks=None,
    yticklabels=None, ytick_labelsize=12, cbar=False, cbar_kws=None, cbar_labelsize=8, fname=None, quality=100,
    transparent=True, bbox_inches='tight', pad_inches=0.1):
    cbar_kws = cbar_kws or {'orientation': 'vertical'}

    plt.figure(figsize=figsize)

    plt.rcParams['axes.labelsize'] = axes_labelsize
    plt.rcParams['axes.titlesize'] = axes_titlesize
    plt.rcParams['xtick.labelsize'] = xtick_labelsize
    plt.rcParams['ytick.labelsize'] = ytick_labelsize

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

    out_h, out_xedges, out_yedges, out_image = plt.hist2d(
        x, y, bins=bins, range=ranges, density=density, cmap=cmap, norm=norm, vmin=vmin, vmax=vmax, alpha=alpha
    )

    if cbar:
        colorbar = plt.colorbar(**cbar_kws)
        colorbar.ax.tick_params(labelsize=cbar_labelsize)

    if fname is not None:
        plt.savefig(fname, quality=quality, transparent=transparent, bbox_inches=bbox_inches, pad_inches=pad_inches)

    return out_h, out_xedges, out_yedges, out_image
