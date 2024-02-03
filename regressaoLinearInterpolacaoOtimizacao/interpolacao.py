import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import *
# muitas estruturas de construção são baseadas em uma parábola. Obtenha graficamente a parábola relacionada à estrutura de uma ponte que tem 20 metros de comprimento e 7 metros de altura
x=[0,10,20]
y=[0,7,0]
f=interp1d(x,y,kind='quadratic')
l=lagrange(x,y) # função interpoladora
xi=np.linspace(1,20,100)
yi=f(xi)
plt.plot(x,y,'o')
plt.plot(xi,yi)
print(l) # polinômio y=-0.07x²+1.4x
plt.show()
