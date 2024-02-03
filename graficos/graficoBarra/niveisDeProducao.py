import matplotlib.pyplot as plt
#tabela a seguir represetan os níveis de produção de pares de um determinado modelo de calçado nos meses de março a julho
# [mês,         março,      abril,  maio,   junho,  julho ]
# [produção,    35.000,    29.000,  27.000, 32.000, 33.000]
#gráfico dos níveis de produção de cada mês
x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
largura = 0.5 # definir largura
plt.bar(x,y, largura)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
# para fazer barras horizontais
# plt.barh(x,y, largura)
# plt.xlabel('produção')
# plt.ylabel('mês')
plt.show()