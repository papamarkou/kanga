import arviz as az

# x is a numpy array of 3 dimensions, (chain, MC iteration, parameter)
def uni_arviz_rhat(x, var_names=None, method='folded', vars=None):
    return [az.rhat(x.transpose()[i].transpose(), var_names=var_names, method=method) for i in vars or range(x.shape[2])]
