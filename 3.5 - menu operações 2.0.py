#Escreva um programa que exiba uma lista de opções (menu): adição,subtração, divisão, multiplicação
#e sair. Imprima a tabuada da operação escolhida.Repita até que a opção saída seja escolhida.1]
while True:
    x = 0
    opcao = int(input('\nDigite a operação que deseja realizar:\n(1)ADIÇÃO \n(2)SUBTRAÇÃO \n(3)DIVISÃO '
                      '\n(4)MULTIPLICAÇÃO \n(5)SAIR'))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        if opcao == 1:
            num = int(input('Digite o número que deseja ver a tabuada de soma: '))
            while x <= 10:
                print(f'{num} + {x} = {num + x}')
                x += 1
        elif opcao == 2:
            num = int(input('Digite o número que deseja ver a tabuada de subtração: '))
            while x <= 10:
                print(f'{num} - {x} = {num - x}')
                x += 1
        elif opcao == 3:
            num = int(input('Digite o número que deseja ver a tabuada de divisão: '))
            while x <= 10:
                if x == 0:
                    x += 1
                print(f'{num} / {x} = %f.2f' % (num / x))
                x += 1
        elif opcao == 4:
            num = int(input('Digite o número que deseja ver a tabuada de multiplicação: '))
            while x <= 10:
                print(f'{num} x {x} = {num * x}')
                x += 1
    else:
        print('Número digitado \033[31mINCORRETO\033[m. Tente novamente:')
