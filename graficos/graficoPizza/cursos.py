import matplotlib.pyplot as plt
# em uma instituição de ensino, há 340 estudantes do curso de Engenharia da Computação, 560 de Engenharia Elétrica e 290 de Engenharia de Produção cursando a disciplina de Geometria Analítica.
x = [340, 560, 290]
cursos = ['Computação', 'Elétrica', 'Produção']
cores=['r', 'm', 'y'] # cria cores personalizadas
plt.axis('equal')
plt.pie(
    x, # os valores que vão compor a pizza
    labels=cursos, # são os cursos que aparece em volta
    colors=cores, # entrega as cores com base na variável declarada
    shadow=True, # cria sombras
    explode=(0.1,0,0), # cria um destaque
    autopct='%1.1f%%' # adiciona porcentagem
)
plt.title('Número de estudantes por curso')
plt.show()