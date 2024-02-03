from sympy import *
# uma indústria de carne congelada realizou um estudo e chegou à conclusão de que o lucro mensal L(x) é dado em função do preço x do quilo da carne congelada, e essa relação é descrita pela função L(x)=-120x²+4800x
x, L = symbols("x L")
L=-120*x**2+4800*x
df=diff(L, x)
d2f=diff(L, x, 2)
p=solve(Eq(df, 0))
ds=d2f.subs(x, p[0])
print('Preço ótimo: ', p[0])
print('Derivada segudna: ', ds)
