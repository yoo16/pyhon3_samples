from sympy import *
import numpy as np
import sys

a, b, c, d, e, f = map(float, input('Please input a, b, c, d, e, f\n').split())

var("a:z")  

func = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
print(func)

result = solve(func, x)
print(result)

#init_printing()
#display(result)