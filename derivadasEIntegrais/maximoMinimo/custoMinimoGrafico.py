import matplotlib.pyplot as plt
import numpy as np
from sympy import *
x, c = symbols("x c")
x = np.linspace(0, 25, 100)
c=x**2-20*x+300
plt.plot(x,c)
plt.show()
