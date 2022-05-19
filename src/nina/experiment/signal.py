import numpy as np
class Signal:
    def __init__(self, detector, source, prob, histogram, background = [], signal_name = "neutrino", norm = 1):
        self.detector = detector
        self.source = source
        self.prob = prob
        self.histogram = histogram
        self.background = background
        self.norm = norm
        self.signal_name = signal_name
    
    # Do simulation
    def simulate(self):
        event = []
        for bin in self.histogram.bins:
            bin_event = self.getEventInBin(bin)
            event.append( self.norm*bin_event )
        return np.array(event)
    
    # Calculate integral in the bin (Simpson rule)
    def getEventInBin(self, bin):
        dE = (bin.max-bin.min)/6
        Emin = bin.min
        Emax = bin.min
        Emean = (Emin+Emax)/2
        distance = self.detector.distanceFrom(self.source)
        #Applying the formula
        result = 0
        for energy, weight in zip( [Emin, Emean, Emax] , [1,4,1] ):
            xsec = self.detector.getXsec(energy)
            flux = self.source.getFlux(energy, distance)
            prob = self.prob.calculate(energy)
            result += weight * ( xsec * flux * prob ) * dE
        result = result*self.norm
        self.events = result
        return result

