import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig=plt.figure()
ax=plt.axes(projection='3d')
Z = np.linspace(0,15,1000)
X = np.sin(Z)
Y = np.cos(Z)
ax.plot3D(X, Y, Z, 'red')
plt.show()