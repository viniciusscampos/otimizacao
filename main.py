from functions import *
from utils import *
from methods import *


gradient_csv_header = ['x0','Iter.','Opt. Point','Opt. Value','Error']

function_one = function_one()
function_two = function_two()
first_derivative_function_one= function_one_first_derivative()
first_derivative_function_two= function_two_first_derivative()
function_one_second_derivative= function_one_second_derivative()
function_two_second_derivative= function_two_second_derivative()

fone_optimal_result = 1.32776
ftwo_optimal_result = 1.22464

xs_f1 = [[0.1,0.1],[0.2,0.2],[0.3,0.3],[0.45,0.51],[0.6,0.6],[0.7,0.7],[0.8,0.8]]
xs_f2 = [[0.1,0.1],[0.2,0.2],[0.3,0.3],[0.45,0.51],[0.6,0.6],[0.7,0.7],[0.8,0.8]]

n = 0.60
y = 0.8

gradient_f1 = []
newton_f1 = []
qnewton_f1 = []

gradient_f2 = []
newton_f2 = []
qnewton_f2 = []

for i in range(len(xs_f1)):
    gradient_f1.append(gradient_method(function_one,first_derivative_function_one,
                    xs_f1[i],n,y,fone_optimal_result,10000))
    
    newton_f1.append(newton_method(function_one,function_one_second_derivative,
        first_derivative_function_one,xs_f1[i],n,y,fone_optimal_result,10000))

    qnewton_f1.append(quase_newton_method(function_one,first_derivative_function_one,
        xs_f1[i],n,y,fone_optimal_result))

    gradient_f2.append(gradient_method(function_two,first_derivative_function_two,
                    xs_f2[i],n,y,ftwo_optimal_result,10000))
    
    newton_f2.append(newton_method(function_two,function_two_second_derivative,
        first_derivative_function_two,xs_f2[i],n,y,ftwo_optimal_result,10000))

    qnewton_f2.append(quase_newton_method(function_two,first_derivative_function_two,
        xs_f2[i],n,y,ftwo_optimal_result))

construct_gradient_csv("results/function1_gradient.csv",gradient_csv_header,gradient_f1)
construct_gradient_csv("results/function1_newton.csv",gradient_csv_header,newton_f1)
construct_gradient_csv("results/function1_qnewton.csv",gradient_csv_header,qnewton_f1) 

construct_gradient_csv("results/function2_gradient.csv",gradient_csv_header,gradient_f2)
construct_gradient_csv("results/function2_newton.csv",gradient_csv_header,newton_f2)
construct_gradient_csv("results/function2_qnewton.csv",gradient_csv_header,qnewton_f2)

#print(gradient_method(function_two,first_derivative_function_two,x,n,y))
#print(newton_method(function_one,function_one_second_derivative,first_derivative_function_one,x,n,y))
#print(newton_method(function_two,function_two_second_derivative,first_derivative_function_two,x,n,y))
#print(quase_newton_method(function_one,first_derivative_function_one,x,n,y))
#print(quase_newton_method(function_two,first_derivative_function_two,x,n,y))