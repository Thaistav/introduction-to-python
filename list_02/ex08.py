#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1=float(input('Informe o valor do primeiro produto: '))
p2=float(input('Informe o valor do segundo produto: '))
p3=float(input('Informe o valor do terceiro produto: '))

menor=p1
if p2<menor:
    p2=menor
if p3<menor:
    p3=menor
print('Você deve comprar o produto no valor de R$ {} '.format(menor))
