'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
n1=float(input('PRIMEIRO NÚMERO: '))
n2=float(input('SEGUNDO NÚMERO: '))
op=int(input('Qual operação deseja fazer:\n1- ADIÇÃO\n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n '))

if op == 1:
    adição=(n1+n2)
    print('A soma de {} +{} = {}'.format(n1,n2,adição))
    if adição % 2 == 0:
        print('{} É um numero par'.format(adição))
    else:
        print('{} É um numero ímpar'.format(adição))
    if adição >= 0:
        print('{} É um numero positivo'.format(adição))
    else:
        print('{} É um numero negativo'.format(adição))
    if adição != round (adição):
        print('{} É um numero decimal'.format(adição))
    else:
        print('{:.0f} É inteiro'.format(adição))
if op == 2:
    sub=(n1-n2)
    print('A subtração de {} - {} = {}'.format(n1,n2,sub))
    if sub % 2 == 0:
        print('{} É um numero par'.format(sub))
    else:
        print('{} É um numero ímpar'.format(sub))
    if sub >= 0:
        print('{} É um numero positivo'.format(sub))
    else:
        print('{} É um numero negativo'.format(sub))
    if sub != round (sub):
        print('{} É um numero decimal'.format(sub))
    else:
        print('{:.0f} É inteiro'.format(sub))
if op == 3:
    mul=(n1*n2)
    print('A multiplicação de {} * {} = {}'.format(n1,n2,mul))
    if mul % 2 == 0:
        print('{} É um numero par'.format(mul))
    else:
        print('{} É um numero ímpar'.format(mul))
    if mul >= 0:
        print('{} É um numero positivo'.format(mul))
    else:
        print('{} É um numero negativo'.format(mul))
    if mul != round (mul):
        print('{} É um numero decimal'.format(mul))
    else:
        print('{:.0f} É inteiro'.format(mul))
if op == 4:
    div=(n1/n2)
    print('A divisão de {} / {} = {}'.format(n1,n2,div))
    if div % 2 == 0:
        print('{} É um numero par'.format(div))
    else:
        print('{} É um numero ímpar'.format(div))
    if div >= 0:
        print('{} É um numero positivo'.format(div))
    else:
        print('{} É um numero negativo'.format(div))
    if div != round (div):
        print('{} É um numero decimal'.format(div))
    else:
        print('{:.0f} É inteiro'.format(div))
else:
    print('OPERAÇÃO INVALIDA')
    exit()
    
