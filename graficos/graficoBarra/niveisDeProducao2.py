import matplotlib.pyplot as plt
import numpy as np
#tabela a seguir representa os níveis de produção de dois modelos pares de um determinado modelo de calçado nos meses de março a julho
# [mês,         março,      abril,      maio,       junho,      julho]
# [produção1,    35.000,    29.000,     27.000,    32.000,    33.000]
# [produção2,    34.000,    33.000,     25.000,    37.000,    27.000]
#gráfico dos níveis de produção de cada mês
mes=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
x=np.arange(5) # arranjo
y1=[35000,29000,27000,32000,33000]
y2=[34000,33000,25000,37000,27000]
largura = 0.3
plt.bar(x, y1, largura, color='r')
plt.bar(x+largura, y2, largura, color='c')
plt.xticks(x, mes)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.legend(['Prod 1', 'Prod 2'], loc=1)
plt.show()