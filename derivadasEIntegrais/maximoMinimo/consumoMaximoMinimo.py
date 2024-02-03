from sympy import *

# a função f(x)=-0.04185x^4+2.52027x³-54.81718x²+509.27586x-1624.86959 descreve a variação do consumo de lanches em uma praça de alimentação de um centro comercial onde x é o horário, das 12 às 22 horas, e f(x) é o respectivo consumo em unidades vendidas
x, f = symbols("x f")
f = -0.04185 * x ** 4 + 2.52027 * x ** 3 - 54.81718 * x ** 2 + 509.27586 * x - 1624.86959
df = diff(f, x)
d2f = diff(f, x, 2)
p = solve(Eq(df, 0))
print(p)
print('Mínimo: ', p[1])
print('Máximo: ', p[2])
