#Escreva um programa que leia um número e veriﬁque se é ou nãoum número primo.
# Para fazer essa veriﬁcação, calcule o resto da divisão do númeropor 2 e depois por todos
# os números ímpares até o número lido. Se o resto de umadessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não sãoprimos e que 2 é o único número primo que é par.
c = 0
x = 1
n = int(input('Digite um número inteiro: '))
while x <= n:
    verificador = n % x
    x += 1
    if verificador == 0:
        c += 1
if c >= 3:
    print(f'o número {n} não é \033[31mPRIMO\033[m.')
else:
    print(f'O número {n} é \033[32mPRIMO\033[m.')
