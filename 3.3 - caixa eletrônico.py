#Vejamos como exemplo um programa que leia um valor e que imprima a quanti-dade de cédulas
#necessárias para pagar esse mesmo valor, apresentado na listagem5.14.
#Para simpliﬁcar, vamos trabalhar apenas com valores inteiros e com cédulasde
# R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1
#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
cedula = 50
cont = 0
print('='*40)
print('{:^40}'.format('CAIXA ELETRÔNICO: SAQUE'))
print('='*40)
saque = int(input('Digite o valor que você deseja sacar: '))
total = saque
while True:
  if total >= cedula:
    total -= cedula
    cont += 1
  else:
    if cont > 0:
      print(f'{cont} cédulas de R${cedula}')
    if cedula == 50:
      cedula = 20
      cont = 0
    elif cedula == 20:
      cedula = 10
      cont = 0
    elif cedula == 10:
      cedula = 1
      cont = 0
    if total == 0:
      break
print('='*40)
print('{:^40}'.format('VOLTE SEMPRE!'))
print('='*40)


