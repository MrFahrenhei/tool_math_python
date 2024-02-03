import matplotlib.pyplot as plt
#tabela a seguir represetan os níveis de produção de pares de um determinado modelo de calçado nos meses de março a julho
# [mês,         março,      abril,  maio,   junho,  julho ]
# [produção,    35.000,    29.000,  27.000, 32.000, 33.000]
#gráfico dos níveis de produção de cada mês
x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y)
# plt.plot (x, y, 'r o') # gráfico só com pontos e se ativado com a linha de cima mistura linha com pontos
# plt.plot(x, y, 'r', linewidth=3) #altera a cor e aumenta o peso da linha
plt.ylim(0, 40000) # define a variação ao eixo y começando do 0
# plt.bar(x,y, largura)
# plt.barh(x,y, largura)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show()