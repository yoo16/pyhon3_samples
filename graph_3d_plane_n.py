from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

def plane(x, y, n, a, b, c):
    return a*x**n + b*y**n + c

print('Graph: ax^n + bx^n + c')
n = int(input('Please input n\n'))

if (n <= 0):
    sys.exit('invalid n!')

a, b, c = map(float, input('Please input a, b, c\n').split())

min_value, max_value, step = map(float, input('Please input min, max, step number\n').split())

if (min_value >= max_value):
    sys.exit('invalid min, max!')

if (step <= 0):
    sys.exit('invalid step!')

x = np.arange(min_value, max_value, step)
y = np.arange(min_value, max_value, step)

X, Y = np.meshgrid(x, y)
Z = plane(X, Y, n, a, b, c)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z)
plt.title("%sx^%s + %sy^%s + %s" % (a, n, b, n, c))
plt.show()
