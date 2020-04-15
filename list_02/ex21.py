'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.'''
print('='*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('='*30)
valor=int(input('Informe o valor do saque: R$  '))

if valor < 10:
    print('OPERAÇÃO INVALIDA\n POR FAVOR, REFAÇA SUA OPERAÇÃO COM OUTRO VALOR! ')
elif valor > 600:
    print('OPERAÇÃO INVALIDA\n POR FAVOR, REFAÇA SUA OPERAÇÃO COM OUTRO VALOR!')
else:
    cem=int(valor/100)
    valor = valor - (cem*100)

    cinquenta = int(valor/50)
    valor = valor - (cinquenta*50)

    vinte = int(valor/20)
    valor = valor - (vinte*20)

    dez = int(valor/10)
    valor = valor - (dez*10)

    cinco = int(valor/5)
    valor = valor-(cinco*5)

    dois = int(valor/2)
    valor = valor-(dois*2)

    print('{} NOTAS DE R$ 100'.format(cem))
    print('{} NOTAS DE R$ 50'.format(cinquenta))
    print('{} NOTAS DE R$ 20'.format(vinte))
    print('{} NOTAS DE R$ 10'.format(dez))
    print('{} NOTAS DE R$ 5'.format(cinco))
    print('{} NOTAS DE R$ 2'.format(dois))

