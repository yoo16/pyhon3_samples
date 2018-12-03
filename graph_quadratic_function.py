import matplotlib.pyplot as plt
import numpy as np
import sys

a, b, c = map(float, input('Please input a, b, c\n').split())

min_x, max_x, step = map(float, input('Please input min x, max x, step number.\n').split())

if (min_x >= max_x):
    sys.exit('invalid min x max x!')
    
if (step <= 0):
    sys.exit('invalid step!')

x = np.arange(min_x, max_x, step)

y = a*x**2 + b*x + c

plt.plot(x, y)
plt.show()