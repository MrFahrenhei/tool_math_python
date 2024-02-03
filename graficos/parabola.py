import matplotlib.pyplot as plt
import numpy as np
x=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y=[25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
x = np.linspace(-5, 5, 100)
y = x ** 2
plt.plot(x, y)
plt.show()