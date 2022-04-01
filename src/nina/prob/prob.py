class Prob():
    '''Recebe params (lista de parametros), func (funcao de probabilidade)'''
    def __init__(self, params, func):
        self.params = params
        self.func = func
    def calculate(self, energy):
        return self.func(energy)