import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import sys

def convertFloat(value):
    value = (S(value).as_coeff_Add())
    real_value = value[0]
    if (type(real_value) == Float):
        return real_value

def answer(a, b, c, d):
    x = Symbol('x')
    values = []
    for value in solve(a*x**3 + b*x**2 + c*x + d):
        values.append(convertFloat(value))
    return values

def plotX(max_x, min_x, step):
   return np.arange(min_x, max_x, step)

def plotY(x, a, b, c, d):
   return a*x**3 + b*x**2 + c*x + d

a, b, c, d = map(float, input('Please input a, b, c, d.\n').split())
min_x, max_x, step = map(float, input('Please input min x, max x, step number.\n').split())

if (min_x >= max_x):
    sys.exit('invalid min x max x!')
    
if (step <= 0):
    sys.exit('invalid step!')

plot_x = plotX(max_x, min_x, step)
plot_y = plotY(plot_x, a, b, c, d)

x = answer(a, b, c, d)
for value in x:
    value = convertFloat(value)
    plt.scatter([value], [0], label = 'x = %s' % value)

plt.plot(plot_x, plot_y)
plt.grid(color='gray')
plt.title("%sx^3 + %sx^2 + %sx + %s" % (a, b, c, d))
plt.legend()
plt.show()