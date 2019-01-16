import numpy as np
from numpy.random import rand
import time

def execFor(N, a, b):
    c = np.array([[0] * N for _ in range(N)])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i][j] = a[i][k] * b[k][j]
    return c

def execDot(N, a, b):
    c = np.array([[0] * N for _ in range(N)])
    c = np.dot(a, b)
    return c

N = 100
a = np.array(rand(N, N))
b = np.array(rand(N, N))

print('---- for ---')
start = time.time()
execFor(N, a, b)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

print('---- dot ---')
start = time.time()
execDot(N, a, b)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")