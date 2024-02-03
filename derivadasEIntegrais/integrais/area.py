from sympy import *
# seja a função f(x)=x², obtenha a área entre o gráfico de f e o eixo de x no intervalo [0,2]
x, f = symbols("x f")
f=x**2
print(integrate(f,(x,0,2)))