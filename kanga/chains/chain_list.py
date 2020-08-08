import numpy as np

class ChainArray:
    def __init__(self, vals):
        self.reset(vals)

    def reset(self, vals):
        self.vals = vals

    @classmethod
    def from_file(selfclass, path, keys=['sample', 'target_val', 'accepted'], dtype=np.float64):

        vals = {}
        not_converted = []

        for key in keys:
            if key in ('accepted', 'target_val', 'sample', 'grad_val'):

                # To do: read path.joinpath(key+'.csv') to array
            else:
                not_converted.append(key)

        return selfclass(vals), not_converted
