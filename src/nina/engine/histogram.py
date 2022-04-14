import numpy as np

class Bin:
    def __init__(self, min, max):
        self.min = min
        self.max = max

class Histogram:
    def __init__(self, bins) -> None:
        self.bins = []
        for i in range( len(bins)-1 ):
            new_bin = Bin(bins[i],bins[i+1])
            self.bins.append( new_bin )
    @staticmethod
    def getUniform(min, max, n_div):
        bins = np.linspace(min, max, n_div)
        hist = Histogram(bins)
        return hist