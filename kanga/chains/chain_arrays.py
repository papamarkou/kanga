import numpy as np

import kanga.stats as st

from .chain_array import ChainArray

class ChainArrays:
    def __init__(self, vals):
        self.reset(vals)

    def reset(self, vals):
        self.vals = vals

    @classmethod
    def from_chain_array(selfclass, chain_arrays, keys=['sample', 'target_val', 'accepted']):
        common_keys = set.intersection(*[set(chain_array.vals.keys()) for chain_array in chain_arrays])
        class_keys = set(keys) & common_keys

        vals = {}

        for key in class_keys:
            vals[key] = np.stack([chain_array.vals[key] for chain_array in chain_arrays])

        return selfclass(vals=vals)

    @classmethod
    def from_file(selfclass, paths, keys=['sample', 'target_val', 'accepted'], dtype=np.float64):
        chain_arrays = []

        for path in paths:
            chain_arrays.append(ChainArray.from_file(keys=keys, path=path, dtype=dtype))

        return selfclass.from_chain_array(np.stack(chain_arrays), keys=keys)

    def __repr__(self):
        return f"{len(self)} Markov chains, each containing {self.num_samples()} samples."

    def __len__(self):
        return self.num_chains()

    def num_params(self):
        return len(self.vals['sample'][0][0])

    def num_samples(self):
        return len(self.vals['sample'][0])

    def num_chains(self):
        return len(self.vals['sample'])

    def get_samples(self):
        return np.stack([self.get_chain(i, key='sample') for i in range(self.num_chains())])

    def get_target_vals(self):
        return np.stack([self.get_chain(i, key='target_val') for i in range(self.num_chains())])

    def get_grad_vals(self):
        return np.stack([self.get_chain(i, key='grad_val') for i in range(self.num_chains())])

    def get_chain(self, idx, key='sample'):
        return np.stack(self.vals[key][idx])

    def mean(self):
        return self.get_samples().mean(1)

    def mean_summary(self, g=lambda x: x.mean(0)):
        return g(self.mean())

    def mc_se(self, mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return np.stack([
            st.mc_se(self.get_chain(i, key='sample'), method=method, adjust=adjust, b=b, r=r, rowvar=False)
            if mc_cov_mat is None
            else st.mc_se_from_cov(mc_cov_mat[i])
            for i in range(self.num_chains())
        ])

    def mc_se_summary(self, g=lambda x: x.mean(0), mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return g(self.mc_se(mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r))

    def mc_cov(self, method='inse', adjust=False, b=None, r=3):
        return np.stack([
            st.mc_cov(self.get_chain(i, key='sample'), method=method, adjust=adjust, b=b, r=r, rowvar=False)
            for i in range(self.num_chains())
        ])

    def mc_cov_summary(self, g=lambda m: m.mean(0), method='inse', adjust=False, b=None, r=3):
        return g(self.mc_cov(method=method, adjust=adjust, b=b, r=r))

    def mc_cor(self, mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return np.stack([
            st.mc_cor(self.get_chain(i, key='sample'), method=method, adjust=adjust, b=b, r=r, rowvar=False)
            if mc_cov_mat is None
            else st.cor_from_cov(mc_cov_mat[i])
            for i in range(self.num_chains())
        ])

    def mc_cor_summary(self, g=lambda m: m.mean(0), mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return g(self.mc_cor(mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r))

    def acceptance(self):
        return [sum(self.vals['accepted'][i]) / self.num_samples() for i in range(self.num_chains())]

    def acceptance_summary(self, g=lambda x: sum(x) / len(x)):
        return g(self.acceptance())

    def multi_ess(self, mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return [
            st.multi_ess(
                self.get_chain(i, key='sample'),
                mc_cov_mat=None if mc_cov_mat is None else mc_cov_mat[i],
                method=method,
                adjust=adjust,
                b=b,
                r=r
            )
            for i in range(self.num_chains())
        ]

    def multi_ess_summary(self, g=lambda x: sum(x) / len(x), mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return g(self.multi_ess(mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r))

    def multi_rhat(self, mc_cov_mat=None, method='inse', adjust=False, b=None, r=3):
        return st.multi_rhat(self.get_samples(), mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r)

    def summary(
        self,
        keys=['multi_ess', 'multi_rhat'],
        g_mean_summary=lambda x: x.mean(0),
        g_mc_se_summary=lambda x: x.mean(0),
        g_acceptance_summary=lambda x: sum(x) / len(x),
        g_multi_ess_summary=lambda x: sum(x) / len(x),
        mc_cov_mat=None,
        method='inse',
        adjust=False,
        b=None,
        r=3):
        summaries = {}

        if any(item in keys for item in ['mc_se', 'multi_ess', 'multi_rhat']):
            if mc_cov_mat is None:
                mc_cov_mat = self.mc_cov(method=method, adjust=adjust)

        for key in keys:
            if key == 'mean':
                summaries[key] = self.mean_summary(g=g_mean_summary)
            elif key == 'mc_se':
                summaries[key] = self.mc_se_summary(
                    g=g_mc_se_summary, mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r
                )
            elif key == 'acceptance':
                summaries[key] = self.acceptance_summary(g=g_acceptance_summary)
            elif key == 'multi_ess':
                summaries[key] = self.multi_ess_summary(
                    g=g_multi_ess_summary, mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r
                )
            elif key == 'multi_rhat':
                summaries[key], _, _, _, _ = self.multi_rhat(mc_cov_mat=mc_cov_mat, method=method, adjust=adjust, b=b, r=r)

        return summaries
