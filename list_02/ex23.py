#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num=float(input('DIGITE UM NUMERO: '))
if num != round(num):
    print('{} É um numero decimal'.format(num))
    print('Arredondado para baixo:',round(num-0.5))
    print('Arredondado para cima:',round(num+0.5))
else:
    print('{} É inteiro'.format(num))
