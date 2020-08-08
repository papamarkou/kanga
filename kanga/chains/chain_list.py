import numpy as np

from pathlib import Path

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
            if key in ('sample', 'target_val', 'grad_val', 'accepted'):
                vals[key] = np.loadtxt(
                    Path(path).joinpath(key+'.csv'), dtype=int if key == 'accepted' else dtype, delimiter=','
                )
            else:
                not_converted.append(key)

        return selfclass(vals), not_converted

    def __repr__(self):
        return f"Markov chain containing {len(self.vals['sample'])} samples."

    def __len__(self):
        return len(self.vals['sample'])

    def get_sample(self, i):
        return self.vals['sample'][:, i]

    def get_samples(self):
        return self.vals['sample']

    def get_target_vals(self):
        return self.vals['target_val']

    def state(self, i=-1):
        current = {}
        for key, val in self.vals.items():
            try:
                current[key] = val[i]
            except IndexError:
                print(f'WARNING: chain does not have values for {key}.')
                pass
        return current

# chain_array, _ = ChainArray.from_file('/Users/9tp/tmp/testing', keys=['sample'])
