import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
# seja a função f(x)=x², obtenha a área entre o gráfico de f e o eixo de x no intervalo [0,2]
x = np.linspace(-1, 3, 1000)
f=x**2
plt.plot(x, f, color='blue')
plt.axhline(color='blue')
plt.fill_between(x,f, where=[(x>0) and (x<2) for x in x], color="green")
plt.show()