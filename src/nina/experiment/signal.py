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
        return event
    
    # Calculate integral in the bin
    def getEventInBin(self, bin):
        Emean = (bin.max+bin.min)/2
        dE = (bin.max-bin.min)

        distance = self.detector.distanceFrom(self.source)

        xsec = self.detector.getXsec(Emean)
        flux = self.source.getFlux(Emean, distance)
        prob = self.prob.calculate(Emean)

        result = ( xsec * flux * prob ) * dE
        self.events = result
        return result
