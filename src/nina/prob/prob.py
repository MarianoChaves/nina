from abc import abstractmethod


class Prob:
    '''Recebe params (lista de parametros), func (funcao de probabilidade)'''
    def __init__(self, params, L):
        self.params = params
        self.L = L

    def calculate(self, energy):
        return self.func(energy)
    
    @abstractmethod
    def func(self, energy):
        pass