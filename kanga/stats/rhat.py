import arviz as az

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def rhat(x, var_names=None, method='folded', vars=None):
    return [az.rhat(x.transpose()[i].transpose(), method=method) for i in vars or range(x.shape[2])]
