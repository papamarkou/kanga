import numpy as np

# Definition of batch means: see p. 7, eq. 6 in https://arxiv.org/pdf/0811.1729.pdf

def batch_mean(x, b):
    return [np.mean(x[i*b:((i+1)*b)]) for i in range(len(x) // b)]
