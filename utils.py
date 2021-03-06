import csv

def isclose(x,tol):
    """Recebe um array e uma tolerancia e retorna true se todos os elementos do array forem <= tol e false caso contrario"""
    for element in x:
        if(abs(element) > tol):
            return False
    return True

def invert_array_signal(x):
    """Recebe um array x e retorna um array cujos elementos sao os de x com sinal negativo"""
    r = []
    for element in x:
        r.append(-element)
    return r

def calculate_error(a,b):
    r = [0]*len(a)
    for i in range(len(a)):
        r[i] = abs(a[i]-b[i])
    return r
       
def dot(x,y):
    """Recebe dois vetores (arrays) e retorna o produto escalar entre eles."""
    s = 0
    for i in range(len(x)):
        s= s + x[i]*y[i]
    return s

def escalar_vector_product(x,e):
    """Recebe um vetor (array) e um escalar e retorna um array cujos elementos estao multiplicados pelo escalar (e)"""
    r = []
    for element in x:
        r.append(element*e)
    return r

def sum_vectors(x,y):
    """Recebe dois vetores (arrays) e retorna o vetor cujos elementos sao as somas dos pares de elementos."""
    r = [0,0]
    r[0] = x[0]+y[0]
    r[1] = x[1]+y[1]
    return r    

def determinant(m):
    """Recebe uma matriz 2x2 e retorna o seu determinante"""
    r = (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    return r

def inverse_2d_matrix(m):
    """Recebe uma matriz de 2 dimensoes e retorna a matriz inversa"""
    inverse_m = [[0,0]]*2
    d = determinant(m)
    if(d!=0):
        inverse_m[0][0] = m[1][1]/d
        inverse_m[0][1] = -m[0][1]/d
        inverse_m[1][0] = -m[1][0]/d
        inverse_m[1][1] = m[0][0]/d
    return inverse_m

def matrixXVector(m,v):
    """Vetor v eh um vetor coluna"""
    r = [0,0]
    r[0] = m[0][0]*v[0]+m[0][1]*v[1]
    r[1] = m[1][0]*v[0]+m[1][1]*v[1]
    return r

def vector_tXmatrix(m,v):
    """Vetor a eh um vetor linha e a matriz tem dimensao 2x2 e retorna um vetor coluna"""
    r = [0,0]
    r[0] = v[0]*m[0][0] + v[1]*m[1][0]
    r[1] = v[0]*m[0][1] + v[1]*m[1][1]
    return r    

def vectorXvector_t(a,b):
    """Vetor a eh coluna e o vetor b eh vetor linha"""
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

def csvDictionaryConstruct(a,b):
    """Funcao criada para auxiliar na criacao das tabelas csv com os resultados obtidos."""
    d = {}
    for i in range(len(a)):
        d[a[i]] = b[i]
    return d 

def construct_gradient_csv(csv_absolute_path,csv_header,csv_results):
    """Funcao criada para construcao e escrita no csv"""
    with open(csv_absolute_path,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csv_header)
        
        writer.writeheader()   
        for i in range(len(csv_results)):
            writer.writerow(csvDictionaryConstruct(csv_header,csv_results[i]))