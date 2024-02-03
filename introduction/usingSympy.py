from sympy import *
x, y = symbols("x y")
y = 2 * x
print(y)
print(y.subs(x, 7))