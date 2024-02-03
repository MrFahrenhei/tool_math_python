import matplotlib.pyplot as plt
# em uma indústria, 450 funcionários trabalham no primeiro turno, 580 no segundo turno e 270 no terceiro turno
x = [450, 580, 270]
turnos = ['1º Turno', '2° Turno', '3° Turno']
cores=['r', 'b', 'y'] # cria cores personalizadas
plt.axis('equal')
plt.pie(
    x, # os valores que vão compor a pizza
    labels=turnos, # são os cursos que aparece em volta
    colors=cores, # entrega as cores com base na variável declarada
    shadow=True, # cria sombras
    explode=(0.1,0,0), # cria um destaque
    autopct='%1.1f%%' # adiciona porcentagem
)
plt.title('Número de funcionários por turno')
plt.show()