import matplotlib.pyplot as plt
import matplotlib.patches as patches
# faça a representação de um círculo azul com centro em C(7,6) e raio igual a 5
fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Circle((7,6),5,color='blue'))
plt.ylim(0,15)
plt.xlim(0,15)
plt.show()