from functions import *
from utils import *
from methods import *
import csv

gradient_csv_header = ['x0','Iter.','Opt. Point','Opt. Value','Error']

function_one = function_one()
function_two = function_two()
first_derivative_function_one= function_one_first_derivative()
first_derivative_function_two= function_two_first_derivative()
function_one_second_derivative= function_one_second_derivative()
function_two_second_derivative= function_two_second_derivative()
x = [0.45,0.51]
n = 0.60
y = 0.8

gradiente_fone = gradient_method(function_one,first_derivative_function_one,x,n,y)
with open('results/gradient_f1.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=gradient_csv_header)
    
    writer.writeheader()    
    writer.writerow(csvDictionaryConstruct(gradient_csv_header,gradiente_fone))
    
#print(gradient_method(function_one,first_derivative_function_one,x,n,y))
#print(gradient_method(function_two,first_derivative_function_two,x,n,y))
#print(newton_method(function_one,function_one_second_derivative,first_derivative_function_one,x,n,y))
#print(newton_method(function_two,function_two_second_derivative,first_derivative_function_two,x,n,y))
#print(quase_newton_method(function_one,first_derivative_function_one,x,n,y))
#print(quase_newton_method(function_two,first_derivative_function_two,x,n,y))