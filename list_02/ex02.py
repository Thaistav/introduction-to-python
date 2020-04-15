#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
x=int(input('Digite um valor: '))
if x % 2 ==0:
    print('{} é positivo'.format(x))
else:
    print('{} é negativo'.format(x))
