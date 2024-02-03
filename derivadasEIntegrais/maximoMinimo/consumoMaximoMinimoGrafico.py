import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(12, 22, 100)
f = -0.04185 * x ** 4 + 2.52027 * x ** 3 - 54.81718 * x ** 2 + 509.27586 * x - 1624.86959
plt.plot(x, f)
plt.show()
