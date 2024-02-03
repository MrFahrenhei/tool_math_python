import matplotlib.pyplot as plt
import matplotlib.patches as patches
# faça a representação de uma elipse com centro em C(8,5) em que o diãmetro horizontal seja igual a 7, e o vertical seja igual a 3
fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Ellipse((8,5),7,3,color='blue'))
plt.ylim(0,10)
plt.xlim(0,15)
plt.show()