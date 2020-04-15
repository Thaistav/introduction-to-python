'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

carne=int(input('1 - FILÉ DUPLO\n2 - ALCATRA\n3 - PICANHA\n'))
kilo=float(input('Quantos KG deseja?: '))
pag=int(input('Qual será a forma de pagamento?\n1 - DINHEIRO\n2 - CARTÃO TABAJARA\n3 - OUTRO CARTÃO\n'))

#CARNE TIPO FILE DUPLO
if carne == 1:
    if kilo > 5:
        file=kilo*5.80
        if pag == 2:
            desc=(file*5/100)
            total=file-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: FILÉ DUPLO__________QTD: {}'.format(kilo,total))
            print('PREÇO: R$ {}__________DESCONTO {}'.format(file,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {:.2f}'.format(total))
        elif pag == 1:
            print('{:^30}'.format('CUPOM FISCAL:'))
            print('TIPO: FILÉ DUPLO__________QTD: {}'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: DINHEIRO'.format(file))
        else:
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: FILE DUPLO________QTD: {}__________'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: CARTÃO'.format(file))

    else:
        file=kilo*4.90
        if pag == 2:
            desc=(file*5/100)
            total=file-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: FILÉ DUPLO__________QTD: {} '.format(kilo))
            print('PREÇO: R$ {} DESCONTO {}'.format(file,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {}'.format(total))
        elif pag == 1:
            print(' {-^30CUPOM FISCAL:-^30}')
            print('TIPO: FILÉ DUPLO  QTD: {}  PREÇO: R$ {} FORMA DE PAGAMENTO: DINHEIRO'.format(kilo,file))
        else:
            print('TIPO: FILE DUPLO  QTD: {}  PREÇO: R$ {} FORMA DE PAGAMENTO: CARTÃO'.format(kilo,file))
#CARNE TIPO ALCATRA 
if carne == 2:
    if kilo > 5:
        alca=kilo*6.80
        if pag == 2:
            desc=(alca*5/100)
            total=alca-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: ALCATRA__________QTD: {}'.format(kilo,total))
            print('PREÇO: R$ {}__________DESCONTO {}'.format(alca,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {:.2f}'.format(total))
        elif pag == 1:
            print('{:^30}'.format('CUPOM FISCAL:'))
            print('TIPO: ALCATRA__________QTD: {}'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: DINHEIRO'.format(alca))
        else:
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: ALCATRA________QTD: {}__________'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: CARTÃO'.format(alca))

    else:
        
        if pag == 2:
            alca=kilo*5.90
            desc=(alca*5/100)
            total=alca-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: ALCATRA__________QTD: {} '.format(kilo))
            print('PREÇO: R$ {}__________DESCONTO {}'.format(alca,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {}'.format(total))
        elif pag == 1:
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: ALCATRA__________QTD: {}__________PREÇO: R$ {}__________FORMA DE PAGAMENTO: DINHEIRO'.format(kilo,alca))
        else:
            print('TIPO: ALCATRA__________QTD: {}__________PREÇO: R$ {}__________FORMA DE PAGAMENTO: CARTÃO'.format(kilo,alca))
            
#PICANHA
if carne == 3:
    if kilo > 5:
        picanha=kilo*7.80
        if pag == 2:
            desc=(picanha*5/100)
            total=picanha-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: PICANHA__________QTD: {}'.format(kilo,total))
            print('PREÇO: R$ {}__________DESCONTO {}'.format(picanha,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {:.2f}'.format(total))
        elif pag == 1:
            print('{:^30}'.format('CUPOM FISCAL:'))
            print('TIPO: PICANHA__________QTD: {}'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: DINHEIRO'.format(picanha))
        else:
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: PICANHA________QTD: {}__________'.format(kilo))
            print('PREÇO: R$ {}__________FORMA DE PAGAMENTO: CARTÃO'.format(picanha))
    else:
        if pag == 2:
            picanha=kilo*6.90
            desc=(picanha*5/100)
            total=picanha-desc
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: PICANHA__________QTD: {} '.format(kilo,picanha,desc,total))
            print('PREÇO: R$ {}__________DESCONTO {}'.format(picanha,desc))
            print('FORMA DE PAGAMENTO: CARTÃO TABAJARA__________TOTAL R$ {}'.format(total))
        elif pag == 1:
            print('{:^30}'.format('CUPOM FISCAL'))
            print('TIPO: PICANHA__________QTD: {}__________PREÇO: R$ {}__________FORMA DE PAGAMENTO: DINHEIRO'.format(kilo,picanha))
        else:
            print('TIPO: PICANHA__________QTD: {}__________PREÇO: R$ {}__________FORMA DE PAGAMENTO: CARTÃO'.format(kilo,picanha))
            
        
