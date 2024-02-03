from sympy import *

# a relação entre o preço de venda x de um modelo de aparelho de telefone celular e o lucro y referente à comercialização desse aparelho é dada pela função y=-4x2+4000x-200000
x, y = symbols("x y")
y = -4 * x ** 2 + 4000 * x - 200000
df = diff(y, x)  # derivada
d2f = diff(y, x, 2)  # derivada segunda
p = solve(Eq(df, 0))  # resolver equação igual a zero
l = y.subs(x, p[0])
ds = d2f.subs(x, p[0])
print("Preço ótimo:", p[0])
print("Lucro máximo:", l)
print("Derivada segunda", ds)
