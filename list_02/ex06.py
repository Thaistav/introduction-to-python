#Faça um Programa que leia três números e mostre o maior deles.
n1=int(input('informe um numero: '))
n2=int(input('informe outro: '))
n3=int(input('outro: '))
if n1 > n2 and n1 > n3:
    print("O maior numero é {} ".format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior numero é {} '.format(n2))
else:
    print('O maior numero é {} '.format(n3))
    
