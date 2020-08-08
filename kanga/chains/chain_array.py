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
        return len(self.get_samples())

    def num_params(self):
        return len(self.get_sample(0))

    def get_sample(self, idx):
        return self.vals['sample'][idx, :]

    def get_samples(self):
        return self.vals['sample']

    def get_target_vals(self):
        return self.vals['target_val']

    def get_grad_val(self, idx):
        return self.vals['grad_val'][idx, :]

    def get_grad_vals(self):
        return self.vals['grad_val']

    def state(self, idx=-1):
        current = {}
        for key, val in self.vals.items():
            try:
                current[key] = val[idx]
            except IndexError:
                print(f'WARNING: chain does not have values for {key}.')
                pass
        return current

    def mean(self):
        return self.get_samples().mean(0)

    def acceptance_rate(self):
        return sum(self.vals['accepted'])/len(self.vals['accepted'])

# chain_array, _ = ChainArray.from_file('/Users/9tp/tmp/testing', keys=['sample'])
