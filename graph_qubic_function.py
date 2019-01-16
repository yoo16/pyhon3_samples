import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import sys
 
def convertFloat(value):
    value = (S(value).as_coeff_Add())
    if (type(value[0]) == Float):
        return value[0]
        
def function(a, b, c, d):
    x = Symbol('x')
    return a*x**3 + b*x**2 + c*x + d
 
def answer(a, b, c, d):
    return solve(function(a, b, c, d))

def plots(a, b, c, d, min_x, max_x, step):
    x = np.arange(min_x, max_x, step)
    y = [function(a, b, c, d).subs(Symbol('x'), value) for value in x]
    return x, y
 
step = 0.1
a, b, c, d = map(float, input('Please input a, b, c, d.\n').split())
min_x, max_x = map(float, input('Please input min x, max x.\n').split())
 
if (min_x >= max_x): sys.exit('invalid min x max x!')
 
#fig, ax = plt.subplots()
for value in answer(a, b, c, d):
    value = convertFloat(value)
    #ax.annotate(value, (value, 0))
    plt.scatter([value], [0], label = 'x = %s' % value)

x, y = plots(a, b, c, d, min_x, max_x, step)
plt.plot(x, y)
plt.grid(color='gray')
plt.title("%sx^3 + %sx^2 + %sx + %s" % (a, b, c, d))
plt.legend()
plt.show()