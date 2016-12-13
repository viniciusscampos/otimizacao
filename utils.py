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