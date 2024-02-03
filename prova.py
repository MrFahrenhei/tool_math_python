from sympy import *
import numpy as np

# questão sobre salário
# x, f = symbols("x f")
# f=2324/3
# print(f)

# questão sobre expandri
# x, y = symbols("x y")
# print(expand((2 * x + y) ** 3))

# questão de juros
# c= 566.0
# m=614.3
# n=6
# taxa = ((m-c)/n/c)*100
# print("a taxa é de %.2f%%" % taxa)
# valor = c*taxa/100
# print("o valor é ", valor)

# função receite de uma empresa
# x, r, c = symbols('x r c')
# r = 511 * x
# c = 392 * x + 22500
# p = solve(Eq(r, c), x)
# print(p[0])

#industria dos copos
# x, y = symbols("x y")
# y=27936.10 + 1243.90
# print(y)

# lucro do preço vendido por 350
# x, y = symbols("x y")
# y = -7*x**2+5200*x-80000
# print(y.subs(x, 350))

# PROVA 2
# x,q = symbols("x q")
# q=18*x**4-14*x**2+22*x-1
# print(diff(q, x))

# fabrica de bike
# x, y = symbols("x y")
# y = (1/3)*x+1
# print(y)

# lucro máximo
# x, y = symbols("x y")
# y= 1340*x-0.08*x**2
# df = diff(y, x)
# d2f=diff(y, x, 2)
# p=solve(Eq(df,0))
# l=y.subs(x, p[0])
# ds=d2f.subs(x, p[0])
# print("lucro máximo:", p[0])

# derivada
# x, d = symbols("x d")
# d = 19*x**6-33*x**3+111*x+19
# print(diff(d, x))

x, f = symbols("x f")
f = -4*x**2+40*x-7
coeff=[-4, 40, -7]
r=np.roots(coeff)
a = integrate(f, (x,min(r), max(r)))
print(a)