import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def hasAnswer(a, b, c):
    return ((b * b) - (4 * a * c)) >= 0

def answer(a, b, c):
    x1 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    return [x1, x2]

def plotX(a, b, c):
    max_x = 10
    min_x = -10

    if (hasAnswer(a, b, c)):
        x = answer(a, b, c)
        x1 = x[0]
        x2 = x[1]
        center = (x2 - x1) * 0.5

        band = abs(x2 - x1)
        if band <= 1:
            band = 10

        max_x = round(x1 + band, 0)
        min_x = round(x2 - band, 0)

    x = np.arange(min_x, max_x, 0.1)
    return x

def plotY(a, b, c):
    return a*x**2 + b*x + c

def plotScatterX(plt, a, b, c):
    if (hasAnswer(a, b, c)):
        x = answer(a, b, c)
        plt.scatter([x[0]], [0], label = 'x1 = %s' % x[0])
        plt.scatter([x[1]], [0], label = 'x2 = %s' % x[1])
    return

print('Simulatenous Equations. a * x^2 + b * x + c')
a, b, c = map(float, input('Please input a, b, c\n').split())

x = plotX(a, b, c)
y = plotY(a, b, c)
plt.plot(x, y)

plotScatterX(plt, a, b, c)

plt.title('Function: %sx^2 + %sx + %s' % (a, b, c))

plt.grid(color='gray')
plt.legend()
plt.show()