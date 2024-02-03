from sympy import *
# considerando a função f(x,y) = (1-x²)²+100(y-x²)², faça o gráfico e em seguida determine e classifique os pontos críticos
x, y, f = symbols("x y f")
f=(1-x)**2+2*(3-y)**2
fx=diff(f,x)
fy=diff(f,y)
fxx=diff(f,x,2)
fyy=diff(f,y,2)
fxy=diff(fx,y)
fyx=diff(fy,x)
px=solve(Eq(fx,0))
py=solve(Eq(fy,0))
fxxp=fxx.subs({x:px[0],y:py[0]})
fyyp=fyy.subs({x:px[0],y:py[0]})
fxyp=fxy.subs({x:px[0],y:py[0]})
fyxp=fyx.subs({x:px[0],y:py[0]})
D=fxxp*fyyp-fxyp*fyxp
print('Solução :(%.2f, %.2f)' % (px[0], py[0]))
print('Determinante: ', D)
print('Derivada segunda em relação a x: ', fxxp)