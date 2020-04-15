'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario=float(input('Informe o salário do colaborador: '))
if salario <= 280.0:
    aumento=(20/100)*salario+salario
    valor=(20/100)*salario
    print('Salário atual: R${}\n Percetual de Aumento: 20%\nReajuste: R$ {}'.format(salario,valor))
    print('Novo salario: R$ {}'.format(aumento))
elif salario == 281 or salario <= 700:
    aumento1=(15/100)*salario+salario
    valor1=(15/100)*salario
    print('Salario atual: R$ {}\nPercetual de Aumento: 15%\nValor do aumento: {}'.format(salario,valor1))
    print('Novo salario: R$ {}'.format(aumento1))
elif salario == 701 or salario <= 1500:
    aumento2=(10/100)*salario+salario
    valor2=(10/100)*salario
    print('Salario atual: R$ {}\nPercetual de Aumento: 10%\nValor do aumento: R$ {:.2f}'.format(salario,valor2))
    print('Novo salario: R$ {}'.format(aumento2))
elif salario > 1500.00:
    aumento3=(5/100)*salario+salario
    valor3=(5/100)*salario
    print('Salario atual: R$ {}\nPercetual de Aumento: 5%\n Valor do aumento: R$ {}'.format(salario,valor3))
    print('Novo salario: R$ {}'.format(aumento3))

    
