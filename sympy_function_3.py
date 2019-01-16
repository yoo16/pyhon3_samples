from sympy import *
import numpy as np
import sys

a, b, c, d = map(float, input('Please input a, b, c, d\n').split())

var("a:z")
func = a*x**3 + b*x**2 + c*x + d
print(func)

result = solve(func, x)
print(result)

#terminal $ jupyter notebook
#init_printing()
#display(result)