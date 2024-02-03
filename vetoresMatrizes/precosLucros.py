import numpy as np
# a tabela a seguir apresenta os preços e os lucros, em dólares, referentes a três mercadorias importadas:
# [Item,            Preço de custo,     Lucro unitário]
# [caixa de som,    R$  5.90,           R$ 7.10]
# [carregador       R$ 2.38             R$ 2.52]
# [pen drive        R$ 2.90             R$ 2.00]
# escreva os valores em uma tabela e, sabendo que 1 dólar corresponde a 4.10 reais, obtenha os respectivos valores em reais
A = np.array([
    [5.90, 7.10], [2.38,2.52], [2.90, 2.00]
])
B = 4.10*A
print(B)