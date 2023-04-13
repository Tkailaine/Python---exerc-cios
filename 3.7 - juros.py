#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.Escreva o total ganho com juros no período
dep = float(input('Digite o valor à ser depositado na conta poupaça: '))
juros = float(input('Digite a taxa de rendimento (juros) do banco por mês: '))
m = 1
soma = dep
while m <= 24:
    j = soma * juros/100
    soma = soma + j
    print(f'{m}° mês = R${soma:.2f}')
    m = m + 1
print(f'O Total de juros ganho nesse período é de R${soma - dep:.2f}')
