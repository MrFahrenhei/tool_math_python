import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x=np.linspace(-5, 5, 100)
y=np.linspace(-5, 5, 100)
X,Y= np.meshgrid(x, y)
Z = X**2+y**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
# ax.plot_wireframe(X,Y,Z) # para textura de rede
# ax.contour3D(X,Y,Z, 15) # para curvas de nível
plt.show()