from sympy import *
#em uma indústria, o custo c referente à produção diária de x unidades é de c(x)=x²+2x+300
#sabe-se que o nível de produção dessa indústria é de x(t)=20t unidades durante t horas de trabalho
# expresse o custo de produção em função do tempo
c, x, t = symbols("c x t")
c=x**2+2*x+300
print(c.subs(x, 20*t))
# 400t²+40t+300