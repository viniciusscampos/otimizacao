from math import log,atan

def fone():
    def g(p):
        return log(1 - log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def ftwo():
    def g(p):
        return atan(-log(p[0]*(1-p[0])*p[1]*(1-p[1])))
    return g

def fslide():
    def g(p):
        return (0.5*(p[0]-2)**2 + (p[1]-1)**2)
    return g
    
def gfone():
    def gradiente(p):
        return [(2*p[0]-1)/((p[0]-1)*p[0]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1)), (2*p[1]-1)/((p[1]-1)*p[1]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])-1))]
    return gradiente

def gftwo():
    def gradiente(p):
        return [(1-2*p[0])/((p[0]-1)*p[0]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1)), (1-2*p[1])/((p[1]-1)*p[1]*(log((p[0]-1)*p[0]*(p[1]-1)*p[1])**2+1))]
    return gradiente

def gfslide():
    def gradiente(p):
        return [p[0]-2,2*(p[1]-1)]
    return gradiente

def isclose(x,tol):
    """Recebe um array e uma tolerancia e retorna true se todos os elementos do array forem <= tol e false caso contrário"""
    for element in x:
        if(element > tol):
            return False
    return True

def invert_array_signal(x):
    """Recebe um array x e retorna um array cujos elementos são os de x com sinal negativo"""
    r = []
    for element in x:
        r.append(-element)
    return r
        
def dot(x,y):
    """Recebe dois vetores (arrays) e retorna o produto escalar entre eles."""
    s = 0
    for i in range(len(x)):
        s= s + x[i]*y[i]
    return s

def escalar_vector_product(x,e):
    """Recebe um vetor (array) e um escalar e retorna um array cujos elementos estão multiplicados pelo escalar (e)"""
    r = []
    for element in x:
        r.append(element*e)
    return r

def sum_vectors(x,y):
    """Recebe dois vetores (arrays) e retorna o vetor cujos elementos são as somas dos pares de elementos."""
    r = []
    for i in range(len(x)):
        r.append(x[i] + y[i])
    return r

def armijo(f,gf,x,d,n,y):
    t=1
    while(f( sum_vectors(x, escalar_vector_product(d,t))) > f(x) + n*t*dot(gf(x),d)):
        t= y*t
    return t


def metodo_gradiente(f,gf,x0,n,y):
    k = 0
    xk = x0
    while(not isclose(gf(xk),1e-8) and k<1000):
        dk = invert_array_signal(gf(xk))
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        k = k+1
        xk = xprox        
    return (k,xk,f(xk),gf(xk))    

fone = fone()
ftwo = ftwo()
gfone= gfone()
gftwo= gftwo()
x = [0.45,0.51]
n = 0.25
y = 0.8

print(metodo_gradiente(fone,gfone,x,n,y))
print(metodo_gradiente(ftwo,gftwo,x,n,y))