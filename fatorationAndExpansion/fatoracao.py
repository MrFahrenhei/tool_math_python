from sympy import *
x,y = symbols("x y")
print(factor(x**2+8*x))
print(factor(x*y**3+2*x**2*y**4))
print(factor((x**2-5*x+6)/(x-2)))