import numpy as np

def fone():
    def g(a,b):
        return np.log(1 - np.log(a*(1-a)*b*(1-b)))
    return g

def ftwo():
    def g(a,b):
        return arctan(-np.log(a*(1-a)*b*(1-b)))
    return g
    
def gfone():
    def gradiente(a,b):
        return (2*a-1)/((a-1)*a*(np.log((a-1)*a*(b-1)*b)-1))
    return gradiente

def gftwo():
    def gradiente(a,b):
        return (1-2*a)/((a-1)*a*(np.log((a-1)*a*(b-1)*b)**2+1))
    return gradiente

print(gftwo()(2,2))