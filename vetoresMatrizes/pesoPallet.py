import numpy as np
# em uma transportadora, 10 pallets com 12 caixas cada pesam 844 quilos. nas mesmas condições, 8 pallets com 10 caixas cada um deles pesam 576 quilos. qual é o peso de cada pallet e qual é o peso de cada caixa?
# 10p+120c = 844
# 8p+80c = 576
A = np.array([[10, 120],[8,80]])
b = np.array([[844],[576]])
x = np.linalg.solve(A,b)
print(x)