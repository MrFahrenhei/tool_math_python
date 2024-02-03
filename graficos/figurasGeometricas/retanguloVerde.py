import matplotlib.pyplot as plt
import matplotlib.patches as patches
# construa um retângulo verde com base igual a 5, altura igual a 7 e canto inferior direito no ponto P de coordenadas(2,1)
fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Rectangle((2,1),5,7,color='green'))
plt.ylim(0,10)
plt.xlim(0,10)
plt.show()
