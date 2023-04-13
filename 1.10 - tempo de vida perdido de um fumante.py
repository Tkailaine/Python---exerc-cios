#Escreva um programa para calcular a redução do tempo de vida deum fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anosele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,calcule quantos dias
#de vida um fumante perderá. Exiba o total em dias.
cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input("Digite quantos anos você fuma: "))
total_cigarros= anos * 365 * cigarros
min_perdidos = total_cigarros * 10
dias_perdidos = (min_perdidos /60) /24
print(f'são {dias_perdidos:.0f} dias perdidos')