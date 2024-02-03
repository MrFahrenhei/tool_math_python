from sympy import *
# a relação entre o preço de venda x de um modelo de aparelho de telefone celular e o lucro y referente à comercialização deste aparelho é dada pela função y=-4x²+4000x-200000
# sendo assim, qual é o lucro quando o preço de venda de cada aparelho corresponde a R$ 480,00?
x, y = symbols("x y")
y = -4*x**2+4000*x-200000
print(y.subs(x,480))
#R$ 798.400