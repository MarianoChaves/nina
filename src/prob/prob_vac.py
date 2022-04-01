import numpy as np
from src.prob.prob import Prob

class Prob3nu(Prob):
    __units = 1.27
    l = 1000 #km
    energy = 10 #MeV

    #params[0] = 7.7*10**(-5) #dm21 eV^2 
    #params[1] = 2.7*10**-3 #dm31 eV^2
    #params[2] = 0.18**2 #s13ˆ2
    #params[3] = 0.5 #s23^2
    #params[4] = 0.31 #s12^3


    def __init__(self, params):
        super().__init__(params, self.probee)

    @property  
    def cos2th12(self):
        return 1 - self.params[4]

    @property  
    def cos2th23(self):
        return 1 - self.params[3]

    @property  
    def cos2th13(self):
        return 1 - self.params[2]


    def phi31(self):
        return self.params[1]*self.l/self.energy*self.__units

    def phi21(self):
        return self.params[0]*self.l/self.energy*self.__units

    def phi32(self):
        return (self.params[1]-self.params[0])*self.l/self.energy*self.__units

    def probee(self):
        self.pee = 1-4*self.cos2th12*self.cos2th13**2*self.params[4]*np.sin(self.phi21())**2 - 4*self.cos2th12*self.cos2th13*self.params[4]*np.sin(self.phi31())**2 - 4*self.cos2th13*self.params[4]*self.params[2]*np.sin(self.phi32())**2
        return self.pee


    
