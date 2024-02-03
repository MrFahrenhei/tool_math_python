from scipy.interpolate import *

# uma empresa fez uma ilustração de uma garrafa e precisa obter uma boa estimativa para o seu volume. Para isso, precisa da função que interpola os pontos C,D,E,F,G,H e I.
# obtenha os respectivos polinômio interpolador
x = [4.6, 15.45, 17.72, 10.65, 1.73, 7.69, 0.45]
y = [5.97, 2.11, 2.37, 3.74, 4.94, 5.37, 3.27]
f = lagrange(x,y)
print(f)
