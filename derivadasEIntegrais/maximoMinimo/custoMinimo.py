from sympy import *
# o custo c referente à produção diária de x unidades de certo item corresponde a c(x)=x²-20x+300
x, c=symbols("x c")
c=x**2-20*x+300
df=diff(c,x) #derivar
d2f=diff(c,x,2) #derivada segunda
p=solve(Eq(df,0)) # solução derivada = 0
ds=d2f.subs(x,p[0]) # e positiva ou negativa
print("Produção ótima",p[0])
print("Derivada segunda",ds)