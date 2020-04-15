#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
l1=float(input('Primeiro lado: '))
l2=float(input('Segundo lado: '))
l3=float(input('Terceiro lado:'))

if l1 > (l2+l3) or l2 > (l1+l3) or l3 > (l1+l2):
    print('As medidas não correspondem a um triangulo!')
elif l1 == l2 == l3:
    print('TRIANGULO EQUILATERO!')
elif l1 != l2 != l3:
    print('TRIANGULO ESCALENO!')
elif l1 == l2 or l2 == l3 or l3 == l1:
    print('TRIANGULO ISOSCELES!')
