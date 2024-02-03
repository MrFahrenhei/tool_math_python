# raiz(-15) = raiz(15).raiz(-1)
# raiz(-1) = i
# raiz(-15) = raiz(15i)
# número complexo na forma algébrica: z=a+bi
    # a = parte real:
    # a = Re(z)
    # b = parte imaginária:
    # b = Im(z)

# exemplos
    # a) z=2+7i
    # Re(z)=2
    # Im(z) = 7
    # b) z=4i
    # Re(z) = 0
    # Im(z) = 4
# escreva o número complexo z=3+5j
z = complex(3,5)
print(z)
# obtenha o módulo do número complexo z=3+5j
print(abs(z))
# dados os números complexo z1=3+5j e z2=7-3j, calcule z1+z2, z1.z2 e z1/z2
z1=complex(3,5)
z2=complex(7,-3)
soma=z1+z2
produto=z1*z2
divisao=z1/z2
print(soma)
print(produto)
print(divisao)
