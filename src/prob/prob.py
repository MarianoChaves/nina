class Prob():
    '''Recebe params (lista de parametros), func (funcao de probabilidade)'''
    def __init__(self, params, func):
        self.parms = params
        self.func = func
    def calculate(self, energy):
        return self.func(energy)