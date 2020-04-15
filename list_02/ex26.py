'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros=float(input('Quantos litros gostaria de abastecer? '))
combustivel=input('A-Alcool \n G-Gasolina ')

if litros <= 20 and combustivel == 'A':
    desc=(litros*1.9)-(litros*1.9)*(3/100)
    print('Combustivel:  Alcool - Valor (-3%): R$ {:.2f} '.format(desc))
elif litros > 20 and combustivel == 'A':
    desc=(litros*1.9)-(litros*1.9)*(5/100)
    print("Comnustivel: Alcool  - Valor (-5%): R$ {:.2f}".format(desc))
elif litros <= 20 and combustivel == 'G':
    desc==(litros*2.5)-(litros*2.5)*(4/100)
    print("Combustivel: Gasolina - Valor (-4%): R$ {:.2f}".format(desc))
elif litros > 20 and combustivel == 'G':
    desc=(litros*2.5)-(litros*2.5)*(6/100)
    print("Combustivel: Gasolina - Valor (-6%): R$ {:.2f}".format(desc))
 
