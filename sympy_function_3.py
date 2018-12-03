from sympy import *
import numpy as np
import sys

a, b, c, d = map(float, input('Please input a, b, c, d\n').split())

x = Symbol('x') 
#a = Symbol('a')
#b = Symbol('b')
#c = Symbol('c')
#d = Symbol('d')

result = solve(a*x**3 + b*x**2 + c*x + d, x)
print(result)