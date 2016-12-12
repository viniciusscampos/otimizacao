import numpy as np

def fone():
    def g(p):
        return np.log(1 - np.log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def ftwo():
    def g(p):
        return arctan(-np.log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def fslide():
    def g(p):
        return (0.5*(p[0]-2)**2 + (p[1]-1)**2)
    return g
    
def gfone():
    def gradiente(p):
        return np.array([(2*p[0]-1)/((p[0]-1)*p[0]*(np.log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1)), (2*p[1]-1)/((p[1]-1)*p[1]*(np.log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1))])
    return gradiente

def gftwo():
    def gradiente(p):
        return np.array([(1-2*p[0])/((p[0]-1)*p[0]*(np.log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1)), (1-2*p[1])/((p[1]-1)*p[1]*(np.log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1))])
    return gradiente

def gfslide():
    def gradiente(p):
        return np.array([p[0]-2,2*(p[1]-1)])
    return gradiente

def armijo(f,gf,x,d,n,y):
	t=1
	while(f(x+t*d) > f(x) + n*t*np.dot(np.transpose(gf(x)),d)):
		t= y*t
	return t

f = fslide()
gf = gfslide()
x = np.array([1,0])
d = np.array([3,1])
n = 0.25
t = 1
y = 0.8

print(x +armijo(f,gf,x,d,n,y)*d)
