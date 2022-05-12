import numpy as np

class Bin:
    """
    Class nina.Bin: an histogram bin.

    atributes:
        - min (float): min value of the bin.
        - min (float): max value of the bin.
    """
    def __init__(self, min, max):
        self.min = min
        self.max = max

class Histogram:
    """
    Class nina.Histogram: abstract representation of an histogram.

        - args:
            - bin_list (list): a list of floats with the binning.

        - atributes:
            - bins ([nina.Bin]): a list of bins.
    """
    def __init__(self, bin_list) -> None:
        self.bins = []
        for i in range( len(bin_list)-1 ):
            new_bin = Bin(bin_list[i],bin_list[i+1])
            self.bins.append( new_bin )
    @staticmethod
    def getUniform(min, max, n_div):
        """
        getUniform(min, max, n_div): static method to create an uniform binned histogram.

            - args:
                - min (float): min value of the histogram.
                - max (float): max value of the histogram.
                - n_div (int): number of division of the histogram.

            - returns:
                - histogram (nina.Histogram): the histogram created
        """
        bins = np.linspace(min, max, int(n_div)+1)
        hist = Histogram(bins)
        return hist