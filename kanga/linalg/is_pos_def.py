import numpy as np

def is_pos_def(x):
    if np.array_equal(x, x.transpose()):
        try:
            np.linalg.cholesky(x)
            return True
        except np.linalg.LinAlgError:
            return False
    else:
        return False
