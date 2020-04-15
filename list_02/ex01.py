#Faça um Programa que peça dois números e imprima o maior deles.
n1=int(input('Digite um numero: '))
n2=int(input('Digite outro: '))
if n1 > n2:
    print('{} é o maior! '.format(n1))
else:
    print('{} é o maior! '.format(n2))
