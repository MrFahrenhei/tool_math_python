import matplotlib.pyplot as plt
from sympy import *
import numpy as np
# calcule a área limitada pelo gráfico da função y=-x²+4x+1 e pelo eixo x
x, f = symbols("x f")
f = -x**2+4*x+1
coeff = [-1, 4, 1]
r=np.roots(coeff)
A = integrate(f, (x, min(r), max(r)))
x = np.linspace(min(r)-0.5, max(r)+0.5, 1000)
f = -x**2+4*x+1
plt.plot(x, f, color='blue')
plt.axhline(color='blue')
plt.fill_between(x, f, where=[(x > min(r)) and (x < max(r)) for x in x], color='yellow')
print("área: ", A)
plt.show()