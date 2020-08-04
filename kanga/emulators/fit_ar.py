import numpy as np

from statsmodels.tsa.ar_model import ar_select_order

def fit_ar(x):
    n = len(x)

    ar_selection = ar_select_order(
        x,
        min(int(np.floor(n)), int(np.floor(10 * np.log10(n)))),
        ic='aic',
        trend='n',
        seasonal=False
    )

    order = ar_selection.ar_lags[-1]

    model_fit = ar_selection.model.fit()

    return model_fit.params, model_fit.sigma2, order
