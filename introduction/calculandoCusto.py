from sympy import *
# o custo y de produção de x motocicletas é dado pela função y=0.003x³-0.5x²-50x+5000
# determine o custo referente à produção de 1.100 motocicletas
x, y = symbols("x y")
y = 0.003*x**3-0.5*x**2-50*x+5000
print(y.subs(x,1100))
# R$ 3.338.000,000