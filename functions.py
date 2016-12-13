from math import log,atan

def fone():
    def g(p):
        return log(1 - log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def ftwo():
    def g(p):
        return atan(-log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g
    
def gfone():
    def gradiente(p):
        return [(2*p[0]-1)/((p[0]-1)*p[0]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1)), (2*p[1]-1)/((p[1]-1)*p[1]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1))]
    return gradiente

def gftwo():
    def gradiente(p):
        return [(1-2*p[0])/((p[0]-1)*p[0]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1)), (1-2*p[1])/((p[1]-1)*p[1]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1))]
    return gradiente