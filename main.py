from functions import *
from utils import *
from methods import *

fone = fone()
ftwo = ftwo()
gfone= gfone()
gftwo= gftwo()
x = [0.45,0.51]
n = 0.25
y = 0.8

print(metodo_gradiente(fone,gfone,x,n,y))
print(metodo_gradiente(ftwo,gftwo,x,n,y))