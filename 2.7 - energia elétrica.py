#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de insta-lação: R para residências,
#I para indústrias e C para comércios. Calcule o preço apagar de acordo com a tabela a seguir.

kwh = int(input('Digite quantos KWH foram gastos: '))
instalacao = str(input('Digite o tipo de instalação: \n(R) Residência\n(I) Indústrias\n(C) Comércio')).upper()
if instalacao in 'rR':
    if kwh <= 500:
        valor = kwh * 0.40
        print(f'Valor: {valor:.2f}')
    else:
        valor = kwh * 0.65
        print(f'Valor: {valor:.2f}')
elif instalacao in 'iI':
    if kwh <= 5000:
        valor = kwh * 0.55
        print(f'Valor: {valor:.2f}')
    else:
        valor = kwh * 0.60
        print(f'Valor: {valor:.2f}')
elif instalacao in 'cC':
    if kwh <= 1000:
        valor = kwh * 0.55
        print(f'Valor: {valor:.2f}')
    else:
        valor = kwh * 0.60
        print(f'Valor: {valor:.2f}')