#Modiﬁque o programa anterior para imprimir de 1 até o númerodigitado pelo usuário, mas,
#dessa vez, apenas os números ímpares.
x = 1
num = int(input('Digite um número inteiro para verificar seus ímpares: '))
while x <= num:
    if x%2 != 0:
        print(f'{x}')
    x = x + 1