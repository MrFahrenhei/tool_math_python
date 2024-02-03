import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(0, 300, 100)
y1 = 186 * x1 #função receita
y2 = 109 * x1 + 11200 #função custo
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.show()