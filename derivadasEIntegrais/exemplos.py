from sympy import *
# calcule a derivada primeira de cada uma das seguintes funções
# a) f(x) = -2x³-4x²+13x-1
# b) g(x) = 2x+ln(x)
# c) h(x) = sen(x)
# d) r(x) = tg(x)
# e) q(x) = sen(x)cos(x)
# f) v(x) = raiz(x²-5x)
# g) t(x) = 3x²-4x/2x³+6
x, f, g, h, r, q, v, t= symbols("x f g h r q v t")
f=-2*x**3-4*x**2+13*x-1
g=2*x+ln(x)
h=sin(x)
r=tan(x)
q=sin(x)*cos(x)
v=(x**2-5*x)**(1/2)
t=(3*x**2-4*x)/(2*x**3+6)
print(diff(f,x))
print(diff(g,x))
print(diff(h,x))
print(diff(r,x))
print(diff(q,x))
print(diff(v,x))
print(diff(t,x))
# realizar derivada segunda das questões
print(diff(f,x,2))
print(diff(g,x,2))
print(diff(h,x,2))
