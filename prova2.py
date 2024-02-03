from sympy import *
import numpy as np
from scipy import stats

# f(x)=4x³+12x-7 derivada segunda
x,f,g = symbols("x f g")
f=4*x**3+12*x-7
print(diff(f,x))
print(diff(f,x,2))

# variáveis
    # 5% da produção de automóveis tem defeito
        # dos 5%, 48% são imperceptíveis pelo consumidor ifnal
g=(0.05*0.48)*20000
print(g)

# variáveis
    # [plano,   mensalidade,    adicional]
    # [planoA,  170.0,          25.0     ]
    # [planoB,  110.0,          40.0     ]
# determine o númeo de consultas mensais a serem agendads a fim de que ambos os planos possuam a mesma vantagem financeira
mes_a = 170
mes_b = 110
add_a = 25
add_b = 40
x=(mes_a - mes_b)/(add_a - add_b)
print(x)

#vetores u(3,-2,1) e v(6,5,-7), produto escalar u.v
u = np.array([[3,-2,1]])
v = np.array([[6,5,-7]])
uv = np.inner(u,v)
print(uv[0][0])

# sistema linear com num complexo
# (6+2j)a+(4+j)b=11+3j
# (2-j)a+(2+2j)b=7+4j
A = np.array([
    [complex(6,2), complex(4,1)],
    [complex(2,-1), complex(2,2)]
])
b = np.array([
    [complex(11,3)],
    [complex(7,4)]
])
print(np.linalg.solve(A,b))

# margem de contribuição = preço de venda (147.59) - custo unitário (89.36)
print(147.59-89.36)

#VF = VP x(1+i)^n
# vf = valor futuro
# vp = valor presente
# i = taxa de juros por período
# n = número de períodos
vp = 144010
i = 0.013
n = 14 #meses
vf = vp*(1+i)**n
print(vf)

# reta de regressão A(3,6), B(4,4), C(7,11), D(10,12)
y = np.array([
    [3, 6],
    [4, 4],
    [7, 11],
    [10, 12]
])
a, b, correlacao, p, erro = stats.linregress(y)
print("Reta de regressão: y=%.2fx+%.2f" % (a, b))

print(64700/8)

vp = 6500
i = 0.009
n = 6 #meses
vf = vp*(1+i)**n
print(vf)

#vetores u(7,1,-9) e v(3,-5,-4), produto escalar u.v e uxv
u = np.array([[7,1,-9]])
v = np.array([[3,-5,-4]])
uv = np.inner(u,v)
uxv = np.cross(u,v)
print(uv)
print(uxv)

# sistema linear
# 5x+y+3z=76
# -x+2y+5z=35
# 4x-5y+z=22
contas = np.array([[5,1,3],[-1,2,5],[4,-5,1]])
results = np.array([[76],[35],[22]])
x = np.linalg.solve(contas,results)
print(x)

# estimativa de crescimento populacional
# P=3,1e^0,05t
# P = população em milhões
# e = 2.72
# t = tempo contado em anos
print(3.1*2.72**(0.05*4))

# desenvolva a expressão (12x^5-3x^4+4x²)²
x = symbols("x")
y = (12*x**5-3*x**4+4*x**2)**2
print(expand(y))

# custo c referente a produção diária de x unidades é c(x)2x²+7x+9000
x, y = symbols("x y")
y = 2*x**2+7*x+9000
print(y.subs(x,30))

# sistema linear
# 4x-3y+z=15
# x+y+3z = 27
# 2x+3y-4z = 31
contas = np.array([[4,-3,1],[1,1,3],[2,3,-4]])
results = np.array([[15],[27],[31]])
x = np.linalg.solve(contas,results)
print(x)