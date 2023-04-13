#Faça um programa que leia duas listas e que gere uma terceira comos elementos das duas primeiras
l1 = []
l2 = []
l3 = []
while True:
    nomes = str(input("Digite o nome (SAIR para sair): ")).upper()
    if nomes in 'SAIR':
        break
    else:
        idades = int(input("Digite a idade(0 para sair): "))
    l1.append(nomes)
    l2.append(idades)
l3.extend(l1)
l3.extend(l2)
print(l3)
