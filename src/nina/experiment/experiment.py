from .signal import Signal
class Experiment:
    def __init__(self, signal_list, true_signal_list, signal_errors):
        self.signal_list = signal_list
        self.true_signal_list = true_signal_list
        self.signal_errors = signal_errors

    def setParams(self, params):
        for signal in self.signal_list:
            signal.prob.params = params
        return self