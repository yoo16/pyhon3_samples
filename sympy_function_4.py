from sympy import *
import numpy as np
import sys

a, b, c, d, e = map(float, input('Please input a, b, c, d, e\n').split())

x = Symbol('x') 
#a = Symbol('a')
#b = Symbol('b')
#c = Symbol('c')
#d = Symbol('d')

result = solve(a*x**4 + b*x**3 + c*x**2 + d*x + e, x)
print(result)