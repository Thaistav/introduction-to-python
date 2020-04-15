'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''


import math
A = int(input('Primeiro valor: '))
if A == 0:
    print('Não é uma equação do 2 grau! ')
    exit()
else:
    B = int(input('Segundo valor: '))
    C = int(input('Terceiro valor: '))
    delta = (B**2) - (4*A*C)
if delta < 0:
    print ('Essa equação não possui raizez reais!')
    exit ()
elif delta == 0:
    raiz= (-B/(2*A))
    print('delta = 0\n Raiz: {}'.format(raiz))
else:
    raiz1 = (-B + math.sqrt(delta) ) / (2*A)
    raiz2 = (-B - math.sqrt(delta) ) / (2*A)
    print('A equação possui duas raizes reais: {} e {}'.format(raiz1, raiz2))

