import sys
from pulp import *

# uma importadora pretende comprar pendrives, caixas de som e carregadores para celular. Essa importadora tem 30mil dólares e pretende decidir quantas unidades de cada um desses itens
# irá adquirir de modo a maximizar o lucro referente à posterior venda dessas mercadorias
# [item,            preço de custo,     lucro unitário,     quantidade minima,  quantidade máxima]
# [caixa de som,    5.90,               7.10,               50,                 200]
# [carregador,      2.38,               2.52,               200                    ]
# [pen drive,       2.90,               2.00,               100                    ]
# variáveis:
# x1 = quantidades de caixas de som
# x2 = quantiade de carregadores para celular
# x3 = quantidade de pendrives
# função objetivo: max L =7.10x1+2.52x2+2.00x3
# restrições: 5.90x1+2.38x2+2.90x3<=30000
# x1>=50 e x1<=200
# x2>=200
# x3>=100
prob = LpProblem('Exemplo1', LpMaximize)
x1 = LpVariable("Caixa de som", 0)
x2 = LpVariable("Carregador", 0)
x3 = LpVariable("PenDrive", 0)
prob += 7.1 * x1 + 2.52 * x2 + 2 * x3
prob += 5.9 * x1 + 2.38 * x2 + 2.9 * x3 <= 30000
prob += x1 >= 50
prob += x1 <= 200
prob += x2 >= 200
prob += x3 >= 100
prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Lucro máximo =", value(prob.objective))
