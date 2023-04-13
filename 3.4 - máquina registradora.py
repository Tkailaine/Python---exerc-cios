#Escreva um programa para controlar uma pequena máquina registra-dora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidadecomprada.
# Utilize a tabela de códigos abaixo para obter o preço de cada produto
produto = {}
somador = 0
while produto != 0:
    produto = int(input('Digite o código do produto que deseja comprar (1, 2, 3, 5, ou 9/ Digite 0 para parar): '))
    if produto != 0:
        quantidade = int(input('Digite a quantidade que deseja comprar: '))
        if produto == 1:
            valor = quantidade * 0.50
        elif produto == 2:
            valor = quantidade * 1.00
        elif produto == 3:
            valor = quantidade * 4.00
        elif produto == 5:
            valor = quantidade * 7.00
        elif produto == 9:
            valor = quantidade * 8.00
        else:
            print('Código digitado INCORRETO!')
print(f'R${valor:.2f}')