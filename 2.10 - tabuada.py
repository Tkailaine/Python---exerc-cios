n = int(input('Digite o número que deseja ver a tabuada: '))
i = int(input('Digite o a partir de qual número você deseja ver a tabuada: '))
f = int(input('Digite até qual número (final) você deseja ver a tabuada: '))
print('='*13)
print('{:=^10}'.format(f'TABUADA DO {n}'))
print('='*13)
while i <= f:
    print('{:^10}'.format(f'{n} x {i} = {n*i}'))
    print('='*13)
    i = i + 1