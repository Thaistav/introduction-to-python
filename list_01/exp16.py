'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
metros=int(input('Informe o tamanho da area a ser pintada em metros quadrados: '))
litro=metros/3

if metros%54==0:
    latas=metros/54
else:
    latas=int(metros/54) +1
preco=latas*80
print('Sera necessario {} latas de tinta e custará R$ {:.2f} '.format(latas, preco))
