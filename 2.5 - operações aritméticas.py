#Escreva um programa que leia dois números e que pergunte qualoperação você deseja realizar.
#Você deve poder calcular a soma (+), subtração (-),multiplicação (*) e divisão (/).
#Exiba o resultado da operação solicitada

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
operação = int(input("Digite a operação que você deseja realizar: \n(1) "
                     "SOMA\n(2) SUBTRAÇÃO\n(3) MULTIPLICAÇÃO\n(4) DIVISÃO: "))

if operação == 1:
    resultado = n1 + n2
    print(resultado)
elif operação == 2:
    resultado = n1 - n2
    print(resultado)
elif operação == 3:
    resultado = n1 * n2
    print(resultado)
elif operação == 4:
    resultado = n1 / n2
    print(f'{resultado:.2f}')