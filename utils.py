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
    r = [0,0]
    r[0] = x[0]+y[0]
    r[1] = x[1]+y[1]
    return r    

def determinant(m):
    """Recebe uma matriz 2x2 e retorna o seu determinante"""
    r = (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    return r

def inverse_2d_matrix(m):
    """Recebe uma matriz de 2 dimensões e retorna a matriz inversa"""
    inverse_m = [[0,0]]*2
    d = determinant(m)
    if(d!=0):
        inverse_m[0][0] = m[1][1]/d
        inverse_m[0][1] = -m[0][1]/d
        inverse_m[1][0] = -m[1][0]/d
        inverse_m[1][1] = m[0][0]/d
    return inverse_m

def matrixXVector(m,v):
    """Vetor v é um vetor coluna"""
    r = [0,0]
    r[0] = m[0][0]*v[0]+m[0][1]*v[1]
    r[1] = m[1][0]*v[0]+m[1][1]*v[1]
    return r

def vector_tXmatrix(m,v):
    """Vetor a é um vetor linha e a matriz tem dimensão 2x2 e retorna um vetor coluna"""
    r = [0,0]
    r[0] = v[0]*m[0][0] + v[1]*m[1][0]
    r[1] = v[0]*m[0][1] + v[1]*m[1][1]
    return r    

def vectorXvector_t(a,b):
    """Vetor a é coluna e o vetor b é vetor linha"""
    r = [[0,0],[0,0]]
    r[0][0] = a[0]*b[0]
    r[0][1] = a[0]*b[1]
    r[1][0] = a[1]*b[0]
    r[1][1] = a[1]*b[1]
    return r    

def vector_tXvector(a,b):    
    return dot(a,b)

def matrixXmatrix(m,u):
    r = [[0,0],[0,0]]
    r[0][0] = m[0][0]*u[0][0] + m[0][1]*u[1][0]
    r[0][1] = m[0][0]*u[0][1] + m[0][1]*u[1][1]
    r[1][0] = m[1][0]*u[0][0] + m[1][1]*u[1][0]
    r[1][1] = m[1][0]*u[0][1] + m[1][1]*u[1][1]
    return r

def escalarXmatrix(m,e):
    r = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            r[i][j] = e*m[i][j]
    return r

def soma_matrizes(m,u):
    r = [[0,0],[0,0]]
    for i in range(len(m)):
        for j in range(len(m)):
            r[i][j] = m[i][j] + u[i][j]
    return r

def sub_matrizes(m,u):
    r = [[0,0],[0,0]]
    for i in range(len(m)):
        for j in range(len(m)):
            r[i][j] = m[i][j] - u[i][j]
    return r