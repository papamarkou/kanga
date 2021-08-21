from .cor import cor
from .mean_array_summary import mean_array_summary

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def mean_cor(x):
    return mean_array_summary(x, cor)
