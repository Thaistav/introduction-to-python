'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''
hr=int(input('Informe o valor da hora trabalhada: :  '))
dias=int(input('Informe a quantidade de horas/mes trabalhadas: '))
bruto=hr*dias
IR=(5/100)*bruto
INSS=(10/100)*bruto
FGTS=(11/100)*bruto
total=IR+INSS+FGTS
liquido=bruto-total

if bruto > 2500:  
    print('Salario Bruto: ({}*{})     : R$ {}'.format(hr,dias,bruto))
    print('(-) IR (5%)    : R$ {}'.format(IR))
    print('(-) INSS (10%)    : R$ {}'.format(INSS))
    print('FGTS (11%)    : R$ {}'.format(FGTS))
    print('Total de descontos    : R$ {}'.format(total))
    print('Salario liquido    : R$ {}'.format(liquido))
elif bruto >= 1501  or bruto <= 2500:
    desc=(10/100)*bruto
    liq=bruto - desc
    print('Salario liquido: R$ {}'.format(liq))
elif bruto <= 901 or bruto >= 1500:
    desc=(5/100)*bruto
    liq=bruto - desc
    print('Salario liquido: R$ {}'.format(liq))
elif bruto <= 900:
    print('Trabalhador insento de descontos!')
