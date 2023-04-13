#Escreva um programa que pergunte a quantidade de km percorridospor um carro alugado pelo usuário,
#assim como a quantidade de dias pelos quaiso carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60 pordia e R$ 0,15 por km rodado.
km = float(input("Digite a quantidade de KM rodados: "))
dias = int(input("Digite a quantidade de dias alugados: "))
valor = dias * 60 + km * 0.15
print(f"Valor total à pagar: R${valor:.2f}")