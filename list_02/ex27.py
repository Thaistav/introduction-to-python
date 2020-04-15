'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

fruta=int(input('1 - MORANGO\n2 - MACA\n3 - MORANGO E MAÇA  \n'))

if fruta==3:
    kg_morango=float(input('Quantos KG de Morango deseja?: '))
    kg_maca=float(input('Quantos KG de Maça deseja?: '))

    kg_mm=kg_morango+kg_maca
    preco_mm=(kg_morango*2.5)+(kg_maca*1.8)
    if  kg_mm > 5:
         preco_mm2=(kg_morango*2.2)+(kg_maca*1.5)
         print('R$ {}'.format(preco_mm2))
    elif kg_mm > 8 or preco_mm > 25:
        desconto=(preco_mm2*10/100)-preco_mm2
        print('Total R$ {} com 10% de desconto'.format(desconto))
    else:
        print('Total R$ {}'.format(preco_mm))

if fruta==1:
    kg_mo=float(input('KG MORANGO: '))
    preco_1=2.5*kg_mo

    if kg_mo > 5:
        preco_2=2.2*kg_mo
        if preco_2 > 25:
            desc=(kg_mo*2.2)*(10/100)-kg_mo
            print('Total R$ {} com 10% de desconto'.format(desc))
        else:
            print('Total R$ {}'.format(preco_2))
    elif kg_mo > 8:
        desc=(kg_mo*2.2)*(10/100)-kg_mo
        print('Total R$ {} com 10% de desconto'.format(desc))
    else:
        print('Total R$ {}'.format(preco_1))
    
if fruta==2:
    kg_ma=float(input('KG MACA: '))
    preco_3=1.8*kg_ma

    if kg_ma > 5:
        preco_3=1.5*kg_ma
        if preco_3 > 25:
            desco=(kg_ma*10/100)-kg_ma
            print('R$ {} com 10% de desconto'.format(desco))
        else:
            print('R$ {}'.format(preco_3))

    elif kg_ma > 8:
        desco=(kg_ma*10/100)-kg_ma
        print('R$ {} com 10% de desconto'.format(desco))
    else:
        print('R$ {}'.format(preco_3))

