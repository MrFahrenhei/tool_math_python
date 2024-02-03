import matplotlib.pyplot as plt
from sympy import *
import numpy as np
# qual é a área abaixo da curva y=x³, de x=1 a x=3?
x, f = symbols("x f")
A = integrate(f, (x, 1, 3))
x = np.linspace(0.5, 3.5, 1000)
f = x ** 3
plt.plot(x, f, color='blue')
plt.axhline(color='blue')
plt.fill_between(x, f, where=[(x > 1) and (x < 3) for x in x], color='magenta')
print("área: ", A)
plt.show()