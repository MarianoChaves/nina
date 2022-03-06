from math import pi
class Source():
    '''recebe o fluxo (funcao)'''
    def __init__(self, flux):
        self.flux = flux

    '''calcula o fluxo em funcao da energia e distancia'''
    def getFlux(self, energy, distance):
        return self.flux(energy)/(distance**2*4*pi)