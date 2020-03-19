'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:'''

shora=float(input('Informe quanto você ganha por hora: '))
hora=float(input('Informe quantas horas você trabalho por mês: '))

sbruto=shora*hora
ir=sbruto*11/100
inss=sbruto*8/100
sindicato=sbruto*5/100
sliquido=sbruto-ir-inss-sindicato

print('+ Salario Bruto {}'.format(sbruto))
print('- IR (11%): R$ {}'.format(ir))
print('- INSS (8%) : R$ {}'.format(inss))
print('- Sindicato (5%) R$ {}'.format(sindicato))
print('= Salario liquido : R$ {}'.format(sliquido))



