import numpy as np

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

# %%

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def multi_rhat(x):
    num_chains, num_iters, num_pars = x.shape

    w = np.zeros([num_pars, num_pars])
    for i in range(num_chains):
        w = w + np.cov(x[i], rowvar=False)
    w = w / num_chains

    b = np.cov(np.apply_along_axis(np.mean, 1, c), rowvar=False)
    
    v = ((num_iters - 1) / num_iters) * w + ((num_chains + 1) / (num_chains * num_iters)) * b

    rhat = max(np.linalg.eig(np.matmul(np.linalg.inv(w), v))[0])

    return rhat, v, w, b

# %%

print(multi_rhat(c))
