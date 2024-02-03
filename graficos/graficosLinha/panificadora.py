import matplotlib.pyplot as plt
# [dia,                 segunda,    terça,  quarta,     quinta,     sexta]
# [demanda de pães(kg), 174,        197,    204,        233,        252]
x=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
y=[174, 197, 204, 233, 252]
plt.plot(x, y)
plt.ylim(0, 260)
plt.title('Demandas diárias')
plt.xlabel('Dia')
plt.ylabel('Demanda')
plt.show()