from sympy.plotting import plot
from sympy import Number, NumberSymbol, Symbol, Eq, solve
import sys
 
def function():
    x = Symbol('x')
    return a*x**3 + b*x**2 + c*x + d

a, b, c, d = map(float, input('Please input a, b, c, d.\n').split())
min_x, max_x = map(float, input('Please input min x, max x.\n').split())
 
if (min_x >= max_x): sys.exit('invalid min x max x!')
 
x = Symbol('x')
y = function()

min_y = y.subs([(x, min_x)]) 
max_y = y.subs([(x, max_x)])

plot(y, (x, min_x, max_x))