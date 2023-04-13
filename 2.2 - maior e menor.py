#Escreva um programa que leia três números e que imprima o maiore o menor
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
maior = -9999
menor = 9999
if n1 > maior:
    maior = n1
if n2 > maior :
    maior = n2
if n3 > maior:
    maior = n3

if n1 < menor:
    menor = n1
if n2 < menor :
    menor = n2
if n3 < menor:
    menor = n3
print(f'o maior número é {maior} e o menor {menor}')