from statsmodels.tsa.stattools import acovf

from .fit_ar import fit_ar

def approx_ar_cov_sum(x):
    params, sigma2, order = fit_ar(x)
    param_sum = params.sum()
    asympt_var = sigma2 / ((1 - param_sum) ** 2)

    gammas = acovf(x, nlag=order-1, fft=False)

    if (order != 0):
        Gamma = 0

        for i in range(1, order+1):
            for k in range(1, i+1):
                Gamma = Gamma + params[i-1] * k * gammas[i-k]

        # Gamma is computed using the equation at the bottom of p. 9 in https://arxiv.org/pdf/1804.05975.pdf
        # See also https://stats.stackexchange.com/questions/371792/sum-of-autocovariances-for-arp-model/372006#372006
        Gamma = 2 * (
            Gamma + 0.5 * (asympt_var - gammas[0]) * (params * range(1, order + 1)).sum()
            ) / (1 - param_sum)
    else:
        Gamma = 0

    return Gamma, asympt_var
