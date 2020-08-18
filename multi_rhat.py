# Compute potential scale reduction factor using rhat function of kanga, which is rhat of arviz

# %% Load packages

import numpy as np

from kanga.stats import multi_rhat

# %% Read chains

# chains = genfromtxt('chains01.csv', delimiter=',')

chains = np.array([np.genfromtxt('chain'+str(i+1).zfill(2)+'.csv', delimiter=',') for i in range(4)])

# %%

print(multi_rhat(chains))

# %%

a = np.array([[2.1, 3], [1.5, 6], [4., 5.]])

# a.mean(axis=0)

np.cov(a, rowvar=False)

b = a - a.mean(axis=0)

b.transpose() @ b / 2

c = np.array([
    [[2.1, 3], [1.5, 6], [4., 5.]],
    [[1.5, 5.5], [3.4, 3.], [2., 7,]],
    [[6.5, 1.], [6., 2.9], [4., 5.]],
    [[-3., 2.], [11., 2.], [-5, -6.]]
])

# c.mean(axis=0)
np.mean(c, axis=0)

# d = np.mean(c, axis=1, keepdims=True)
c - np.mean(c, axis=1, keepdims=True)

np.apply_along_axis(np.mean, 0, c)

np.apply_along_axis(np.mean, 0, c - np.mean(c, axis=1, keepdims=True))

np.apply_along_axis(lambda v: np.cov(v, rowvar=False), 0, c)

for i in range(c.shape[0]):
    print(np.cov(c[i], rowvar=False))

dd = [np.cov(c[i], rowvar=False) for i in range(c.shape[0])]

print(multi_rhat(c))
