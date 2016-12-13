import numpy as np

def fone():
    def g(p):
        return np.log(1 - np.log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def ftwo():
    def g(p):
        return np.arctan(-np.log(p[0]*(1-p[0])*p[1]*(1-p[1])))
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

def metodo_gradiente(f,gf,x0,n,y):
    k = 0
    xk = x0
    # array.all() retorna false e ao menos um valor do array for false
    while(not np.isclose([gf(xk)],[1e-10,1e-11]).all()):
        dk = -np.transpose(gf(xk))
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = xk + tk*dk
        k = k+1
        xk = xprox        
    return (k,xk,f(xk),gf(xk))    

fone = fone()
ftwo = ftwo()
gfone= gfone()
gftwo= gftwo()
x = np.array([0.45,0.51])
n = 0.25
y = 0.8

print(metodo_gradiente(fone,gfone,x,n,y))
print(metodo_gradiente(ftwo,gftwo,x,n,y))