from sympy import *
# calcule a integral definida da função f(x) = -2x³-4x²+13x-1 no intervalo [1, 2]
x, f = symbols("x f")
f = -2*x**3-4*x**2+13*x-1
print(integrate(f,(x,1,2)))