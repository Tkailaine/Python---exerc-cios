#Escreva um programa que pergunte o salário do funcionário e calculeo valor do aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de10%.
#Para os inferiores ou iguais, de 15%
salario = float(input('Digite o seu salário: '))
if salario > 1250:
    aumento = (salario * 10/100)
    salario_atual = salario + aumento
    print(f'O valor do aumento será de 10%, R${aumento:.2f}, e o salário ficará R${salario_atual:.2f}')
else:
    aumento = (salario * 15/100)
    salario_atual = salario + aumento
    print(f'O valor do aumento será de 15%, R${aumento:.2f}, e o salário ficará R${salario_atual:.2f}')