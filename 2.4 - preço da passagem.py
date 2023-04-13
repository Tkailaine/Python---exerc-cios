#Escreva um programa que pergunte a distância que um passageirodeseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por kmpara viagens de até de 200 km, e R$ 0,45
#para viagens mais longas.

km = int(input('Digite quantos KM você deseja percorrer: '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f'O valor da passagem ficou \033[31mR${preço:.2f}\033[m.')