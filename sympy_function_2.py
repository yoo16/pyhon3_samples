from sympy import *
import numpy as np
import sys

#a, b, c, d = map(float, input('Please input a, b, c, d\n').split())

var("a:z")

result = solve(a*x**2 + b*x + c, x)

#init_printing()
#display(result)