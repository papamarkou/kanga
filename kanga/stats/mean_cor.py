from functools import reduce
from operator import add

from .cor import cor

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def mean_cor(x):
    return reduce(add, map(lambda m: cor(m), x))/len(x)
