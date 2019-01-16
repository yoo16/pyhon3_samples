from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

def calculateMesh(min_value, max_value, step):
    MESH_COUNT = 20
    x = np.arange(min_value, max_value, step)
    y = np.arange(min_value, max_value, step)
    xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), MESH_COUNT), np.linspace(y.min(), y.max(), MESH_COUNT))
    #xx, yy = np.meshgrid(x, y)
    return xx, yy

def calculateVector(xx, yy, zz):
    return u(xx, yy, zz), v(xx, yy, zz), w(xx, yy, zz)

def plane(x, y, n, a, b, c):
    z = a*x**n + b*y**n + c
    return z

def u(x, y, z):
    return np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)

def v(x, y, z):
    return -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)

def w(x, y, z):
    return (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

print('Graph: ax^n + bx^n + c')
n = int(input('Please input n\n'))

if (n <= 0): sys.exit('invalid n!')

step = 1
a, b, c = map(float, input('Please input a, b, c\n').split())
min_value, max_value = map(float, input('Please input min, max\n').split())
if (min_value >= max_value): sys.exit('invalid min, max!')

xx, yy = calculateMesh(min_value, max_value, step)
zz = plane(xx, yy, n, a, b, c)
u, v, w = calculateVector(xx, yy, zz)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax = Axes3D(fig)
#ax.plot_wireframe(xx, yy, zz)
#ax.plot_wireframe(xx, yx, zz)
#ax.contour(xx, yx, zz, colors=['r','b'])
#ax.plot_surface(xx, yy, zz, alpha=0.9)
ax.quiver(xx, yy, zz, u, v, w, length=0.1, normalize=True, colors=['r'], arrow_length_ratio=0.5)
#ax.scatter3D(xx, yy, zz)
#ax.scatter(xx, yy, zz)
plt.title("%sx^%s + %sy^%s + %s" % (a, n, b, n, c))
plt.show()
