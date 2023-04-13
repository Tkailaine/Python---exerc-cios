#Escreva um programa que leia números inteiros do teclado.
# O pro-grama deve ler os números até que o usuário digite 0 (zero).
# No ﬁnal da execução,exiba a quantidade de números digitados, assim como a soma e a média aritmética
n = {}
somador = 0
c = 0
while n != 0:
    n = int(input('Digite um número inteiro para somarmos e vermos sua média (Digite 0 para parar): '))
    somador = somador + n
    c = c + 1
media = somador / (c-1)
print(f'Você digitou {c - 1} números, a soma deles é igual a {somador} e a média {media:.2f}.')