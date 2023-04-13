#Reescreva o programa anterior para escrever os 10 primeiros múlti-plos de 3
c = 1
x = 1
num = int(input('Digite um inteiro para verificar seus 10° primeiros múltiplos de 3: '))
while c <= 10:
    if x%3 == 0:
        print(x)
        c = c + 1
    x = x +1
