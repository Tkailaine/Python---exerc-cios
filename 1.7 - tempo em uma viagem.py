#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
dis = float(input("Digite a distância do destino (km): "))
vel = float(input("Digite a velocidade média (km/h): "))
tempo = (dis / vel) * 60
if tempo >= 60:
    horas = tempo//60
    min = tempo % 60
    print(f"O tempo gasto para essa viagem será de {horas:.0f} horas e {min:.0f} minutos. ")
else:
    print(f"O tempo gasto será de {tempo} minutos")