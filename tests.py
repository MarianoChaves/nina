from src.nina import *  

if(__name__== "__main__"):
    param = np.zeros(5)

    param[0] = 7.7*10**(-5) #dm21 eV^2 
    param[1] = 2.7*10**-3 #dm31 eV^2
    param[2] = 0.18**2 #s13ˆ2
    param[3] = 0.5 #s23^2
    param[4] = 0.31 #s12^3
    
    p3nu = Prob3nu(param)
    print(p3nu.probee())