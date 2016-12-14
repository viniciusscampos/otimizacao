from utils import *

def armijo(f,gf,x,d,n,y):
    t=1
    while(f( sum_vectors(x, escalar_vector_product(d,t))) > f(x) + n*t*dot(gf(x),d)):
        t= y*t
    return t

def gradient_method(f,gf,x0,n,y):
    k = 0
    xk = x0
    while(not isclose(gf(xk),1e-8) and k<1000):
        dk = invert_array_signal(gf(xk))
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        k = k+1
        xk = xprox        
    return (k,xk,f(xk),gf(xk))    

def newton_method(f,d2f,gf,x0,n,y):
    k = 0
    xk = x0
    dk = [0,0]
    while(not isclose(gf(xk),1e-8) and k<200):
        inverse_hesian = inverse_2d_matrix(d2f(xk))
        first_derivative = gf(xk)
        dk[0] = -(dot(inverse_hesian[0],first_derivative))
        dk[1] = -(dot(inverse_hesian[1],first_derivative))        
        tk = armijo(f,gf,xk,dk,n,y)
        xprox = sum_vectors(xk, escalar_vector_product(dk,tk))
        k = k+1
        xk = xprox        
    return (k,xk,f(xk),gf(xk),d2f(xk))    
