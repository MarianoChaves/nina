from more_itertools import first
from experiment.experiment import Experiment
import numpy as np

class Chi2:
    def __init__(self, experiment: Experiment):
        self.experiment = experiment

    def calculate(self, params):
        chi2 = 0
        simuls = self.experiment.signal_list
        errors = self.experiment.signal_errors
        signals = self.experiment.true_signal_list

        self.experiment.setParams(params)

        for simul, error, signal in zip(simuls, errors, signals):
            chi2 += sum((signal-simul.simulate())**2)/error**2
        return chi2

    def grid_search(self, params):
        chi2=np.zeros(len(params))

        for i in range(len(params)):
            chi2[i] = self.calculate(params[i])
        
        imin = np.argmin(chi2)
        self.experiment.setParams(params[imin])

        return chi2, params[imin]

    def optmizer(self, params_bounds, optmizer):
        run_bounds = []
        for param_bounds in params_bounds:
            if bool(param_bounds):
                run_bounds.append(param_bounds)

        def func(param_run):
            params = self.experiment.signal_list[0].prob.params
            for i in range(len(params_bounds)):
                if bool(param_bounds[i]):
                    params[i] = param_run[i]
            return self.calculate(params)

        return optmizer(func, run_bounds)
