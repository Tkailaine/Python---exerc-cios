#Escreva um programa para aprovar o empréstimo bancário paracompra de uma casa.
#O programa deve perguntar o valor da casa a comprar, osalário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode sersuperior a 30% do salário.
#Calcule o valor da prestação como sendo o valor dacasa a comprar dividido pelo número de meses a pagar

valor = float(input("Digite o valor da casa que você deseja comprar: "))
salario = float(input("Digite seu salário: "))
anos = int(input("Digite em quantos anos você deseja pagar: "))

prestacoes = valor / anos/12
requisito = salario * (30/100)
if prestacoes <= requisito:
    print("Seu empréstimo foi \033[32mAPROVADO\033[m.")
else:
    print("Seu empréstimo foi \033[31mREPROVADO\033[m.")
