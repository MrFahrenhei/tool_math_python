import matplotlib.pyplot as plt
from sympy import *
import numpy as np

# calcule a área limitada pelos gráficos das funções y=2x e y=1/x, com x variando de 1 a 4
x, f, g = symbols("x f g")
f = 2 * x
g = 1 / x
A = integrate((f - g), (x, 1, 4))
x = np.linspace(0.5, 4.5, 1000)
f = 2 * x
g = 1 / x
plt.plot(x, f, color='blue')
plt.plot(x, g, color='red')
plt.axhline(color='black')
plt.fill_between(x, f,g, where=[(x > 1) and (x < 4) for x in x], color='magenta')
print("área: ", A)
plt.show()
