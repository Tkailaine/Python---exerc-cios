#Faça um programa que solicite o preço de uma mercadoria e o per-centual de desconto.
# Exiba o valor do desconto e o preço a pagar
produto = float(input('Digite o valor do produto: '))
porc = float(input('Digite a porcentagem do desconto: '))
desc = produto * (porc/100)
resultado = produto - desc
print(f'O valor do desconto é de R${desc:.2f}, o valor total à pagar é de R${resultado:.2f}. ')