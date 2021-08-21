import itertools
import operator

def running_mean(x):
    return list(map(operator.truediv, itertools.accumulate(x), itertools.count(1)))
