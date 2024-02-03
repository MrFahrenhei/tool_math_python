import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# em uma indústria, a produção nos quatro primeiros meses do ano, respectivamente 5000, 5300, 5200 e 550 unidades.
# obtenha a reta de regressão, o coeficiente de correlação e faça o gráfico contendo os dados originais e a reta de regressão
x = np.array([1,2,3,4])
y = np.array([5000,5300,5200,5500])
a,b,correlacao,p,erro = stats.linregress(x, y)
print("Reta de regressão: y=%.2fx+%.2f" % (a,b))
print("Coeficiente de correlação r=%.2f" % correlacao)
plt.plot(x,y,'o',label="Dados originais")
f=a*x+b
plt.plot(x,f,'r',label="Reta de regressão")
plt.ylim(4900, 5600)
plt.legend()
plt.show()