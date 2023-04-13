#Escreva um programa que pergunte a velocidade do carro de umusuário.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuáriofoi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de80 km/h.
vel = float(input("Digite a velocidade média do carro: "))
if vel > 80:
    multa = (vel - 80) * 5
    print(f"Você foi MULTADO. O valor da multa é de R${multa:.2f}.")
else:
    print("Você não foi multado!")