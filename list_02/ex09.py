#Faça um Programa que leia três números e mostre-os em ordem decrescente
a=int(input('Primeiro numero:'))
b=int(input('Segundo numero: '))
c=int(input('Terceiro numero: '))

if a < b < c:
    print(c,b,a)
if a < c < b:
    print(b,c,a)
if b < c < a:
    print(a,c,b)
if b < a < c:
    print(c,a,b)
if c < b < a:
    print(a,b,c)
if c < a < b:
    print(b,a,c)

