import numpy as np

from matplotlib import cm
from matplotlib.colors import ListedColormap

redblue_cmap = ListedColormap(
    np.vstack((cm.get_cmap('Blues', 128)(np.linspace(1, 0, 128)), cm.get_cmap('Reds', 128)(np.linspace(0, 1, 128)))),
    name='RedBlue'
)
