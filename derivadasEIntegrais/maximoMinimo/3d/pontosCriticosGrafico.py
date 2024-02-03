import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# considerando a função f(x,y) = (1-x²)²+100(y-x²)², faça o gráfico e em seguida determine e classifique os pontos críticos
xx = np.linspace(-5, 5, 100)
yy = np.linspace(-5, 5, 100)
x, y = np.meshgrid(xx, yy)
f=(1-x**2)**2+100*(y-x**2)**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(x, y,f)
plt.show()
