#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano=int(input('INFORME O ANO: '))
if ano % 4 == 0:
    print('Ano Bissexto!')
else:
    print('O ANO INFORMADO NÃO É BISSEXTO')
