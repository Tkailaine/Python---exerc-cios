#Modiﬁque o programa da listagem 6.6 para ler 7 notas em vez de 5
notas = [0,0,0,0,0,0,0]
i = 0
soma = 0
while i < 7:
    notas[i] = float(input(f'Digite a {i+1}° nota: '))
    soma += notas[i]
    i += 1

i = 0
while i < 7:
    print(f'NOTA {i+1}: {notas[i]:.2f}')
    i += 1

print(f'MÉDIA: {soma/i:.2f}')