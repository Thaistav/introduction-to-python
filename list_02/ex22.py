#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
n=int(input('DIGITE UM NÚMERO INTEIRO: '))
if n % 2 == 1:
    print('{} É UM NUMERO ÍMPAR'.format(n))
else:
    print('{} É UM NÚMERO PAR'.format(n))
