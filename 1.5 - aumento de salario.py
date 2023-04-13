#Faça um programa que calcule o aumento de um salário.
#Ele devesolicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumentoe do novo salário.
salario = float(input("Digite o valor do sálario: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))
aumento = salario * (porcentagem/100)
salario_novo = salario + aumento
print(f'O valor do aumento é de R${aumento:.2f} e o salário com aumento é de R${salario_novo:.2f}.')

