from utils import *

def armijo(f,gf,x,d,n,y):
    t=1
    while(f( sum_vectors(x, escalar_vector_product(d,t))) > f(x) + n*t*dot(gf(x),d)):
        t= y*t
    return t

def bfgs_method(hk,p,q):
    aone = 1 +  (vector_tXvector(q,matrixXVector(hk,q)))/(vector_tXvector(p,q))
    atwo = escalarXmatrix(vectorXvector_t(p,p),1/(vector_tXvector(p,q)))
    athree = escalarXmatrix((vectorXvector_t(p,vector_tXmatrix(hk,q)) + matrixXmatrix(hk,vectorXvector_t(q,p))),1/dot(p,q))    
    r = sub_matrizes(soma_matrizes(hk,escalarXmatrix(atwo,aone)),athree)
    return r

def get_p(x_a,x_p):
    """Recebe dois vetores (x_k e x_k+1) retorna um vetor que é a diferença entre eles."""
    return sum_vectors(x_p, invert_array_signal(x_a))
    
def get_q(gf,x_a,x_p):
    """Recebe dois vetores (x_k e x_k+1) e a derivada da função e retorna um vetor que é a diferença entre as derivadas."""
    return sum_vectors(gf(x_p),gf(x_a))
    
def gradient_method(f,gf,x0,n,y,expected_value,num_interations=1000):
    k = 0
    xk = x0
    while(not isclose(gf(xk),1e-8) and k < num_interations):
        dk = invert_array_signal(gf(xk))
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        k = k+1
        xk = xprox        
    return [x0,k,xk,f(xk),abs(f(xk)-expected_value)]

def newton_method(f,d2f,gf,x0,n,y,expected_value,num_interations=1000):
    k = 0
    xk = x0
    dk = [0,0]
    while(not isclose(gf(xk),1e-8) and k<num_interations):
        inverse_hesian = inverse_2d_matrix(d2f(xk))
        first_derivative = gf(xk)
        dk[0] = -(dot(inverse_hesian[0],first_derivative))
        dk[1] = -(dot(inverse_hesian[1],first_derivative))        
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        k = k+1
        xk = xprox        
    return (x0,k,xk,f(xk),abs(f(xk)-expected_value))    


def quase_newton_method(f,gf,x0,n,y,expected_value):
    k = 0
    xk = x0
    dk = [0,0]
    hk = [[1,0],[0,1]]
    p = [1,1]
    while(not isclose(gf(xk),1e-8) and not isclose(p,1e-16)):
        first_derivative = gf(xk)
        dk[0] = -(dot(hk[0],first_derivative))
        dk[1] = -(dot(hk[1],first_derivative))        
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        p = get_p(xk,xprox)
        q = get_q(gf,xk,xprox)
        hprox = bfgs_method(hk,p,q)
        k = k+1
        xk = xprox 
        hk = hprox         
    return (x0,k,xk,f(xk),abs(f(xk)-expected_value))    