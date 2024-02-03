import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

# # função y=3sen(x)+2x³
# x = np.linspace(0, 10)
# y = 3 ** np.sin(x) + 2 * x ** 3
# plt.plot(x, y, color='blue')
# plt.show()

# função z=-2x²+y³
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = -2 * x ** 2 + Y ** 3
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()
