from sympy import *
# um obj desloca-se em linha reta, e a relação entre a distância considerada em metros do obj à origem e o tempo em segundos é dada por s=2t²+3t, determina a velocidade quando t=2seg
s, t = symbols("s t")
s=2*t**2+3*t
ds=diff(s,t)
v=ds.subs(t,2)
print('Velocidade: %.2f m/s' % v)