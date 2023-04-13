#Altere o programa anterior de forma a perguntar também o valordepositado mensalmente.
#Esse valor será depositado no início de cada mês, e vocêdeve considerá-lo para o cálculo
#de juros do mês seguinte

dep = float(input('Digite o valor a ser depositado na poupança: '))
juros = float(input('Digite a taxa de juros por mês: '))
soma = dep
m = 1
while m <= 24:
    j = soma * juros/100
    soma = soma + j
    print(f'O saldo {m}° mês é de R${soma:.2f}')
    m = m + 1
    pergunta = str(input('Deseja adicionar mais algum depósito? '))
    if pergunta in 'sS':
        extra = float(input('Digite o valor a ser depositado: '))
        soma = soma + extra
print(f'O valor ganho com os juros é de R${soma - dep:.2f}')
