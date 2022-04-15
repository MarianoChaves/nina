from nina.engine.object import Object
class Detector(Object):
    '''recebe secao de choque'''
    def __init__(self, xsec, position):
        super().__init__(position)
        self.xsec = xsec

    '''calcula secao de choque em funcao da energia'''
    def getXsec(self, energy):
        return self.xsec(energy)