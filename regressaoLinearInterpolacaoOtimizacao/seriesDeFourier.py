from sympy import *
import matplotlib.pyplot as plt
import numpy as np
# obtenha, por meio da série de Fourier, aproximação para a função y=x utilizando 2, 3 e 4 termos da série.
x,f=symbols("x f")
init_printing()
f=x
s=fourier_series(f,(x, -pi, pi))
x=np.linspace(-np.pi, np.pi, 100)
f=x
y=2*np.sin(x)-np.sin(2*x) # mostra somente com 2 termos
plt.plot(x,y,x,f)
plt.legend(['Aproximação por Fourier', 'Função original'],loc=2)
print(s.truncate(2))
print(s.truncate(3))
print(s.truncate(4))
plt.show()
