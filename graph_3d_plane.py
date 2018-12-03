from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

def plane(x, y, a, b, c):
    z = a*x + b*y + c
    return z

a, b, c = map(float, input('Please input a, b, c.\n').split())

min_value, max_value, step = map(float, input('Please input min, max, step number.\n').split())

if (min_value >= max_value):
    sys.exit('invalid min, max!')
    
if (step <= 0):
    sys.exit('invalid step!')

x = np.arange(min_value, max_value, step)
y = np.arange(min_value, max_value, step)

X, Y = np.meshgrid(x, y)

Z = plane(X, Y, a, b, c)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z)
plt.show()
