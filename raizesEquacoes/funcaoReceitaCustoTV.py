from sympy import *
# uma empresa que fabrica tvs vende cada unidade por R$ 186.00
# o custo para a produção de cada unidade é R$ 109.00
# os custos fixos totais correspondem a R$ 11.200,00 por mês
# função custo: é o que a empresa gasta
# função receita : é o que a empresa está ganhando
x, r, c = symbols('x r c')
r = 186 * x #função receita
c = 109 * x + 11200.0 # função custo
p = solve(Eq(r, c), x) #ponto equilibro
print(p[0]) # função receite
print(r.subs(x, p[0])) # valor da receita