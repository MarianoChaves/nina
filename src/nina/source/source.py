from nina.engine.object import Object
from math import pi
class Source(Object):
    '''recebe o fluxo (funcao)'''
    def __init__(self, flux, position):
        super().__init__(position)
        self.flux = flux

    '''calcula o fluxo em funcao da energia e distancia'''
    def getFlux(self, energy, distance):
        return self.flux(energy)/(distance**2*4*pi)