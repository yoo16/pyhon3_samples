import matplotlib.pyplot as plt
import numpy as np
import sys

a, b, c, d = map(float, input('Please input a, b, c, d.\n').split())
min_x, max_x, step = map(float, input('Please input min x, max x, step number.\n').split())

if (min_x >= max_x):
    sys.exit('invalid min x max x!')
    
if (step <= 0):
    sys.exit('invalid step!')

x = np.arange(min_x, max_x, step)
y = a*x**3 + b*x**2 + c*x + d

plt.plot(x, y)
plt.grid(color='gray')
plt.title("%sx^3 + %sx^2 + %sx + %s" % (a, b, c, d))
plt.legend()
plt.show()