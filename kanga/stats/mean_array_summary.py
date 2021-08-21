from functools import reduce
from operator import add

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def mean_array_summary(x, g):
    return reduce(add, map(g, x))/len(x)
