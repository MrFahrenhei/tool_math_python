from sympy import *
#sabemos que o produto notável (a+b)² pode ser interpretado geometricamente como área de um quadrado de lados iguals "a+b"
#escreva a forma expandida de (a+b)²
a, b = symbols("a b")
print(expand((a+b)**2))
print(expand((a+b)**4))