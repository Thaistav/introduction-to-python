#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno=str(input('Em que turno você estuda: \nM - Matutino\nV - Vespertino\nN - Noturno\n'))


if turno == 'M'.lower():
    print('Bom dia!')
elif turno == 'V'.lower():
    print('Boa tarde!')
elif turno == 'N'.lower():
    print('Boa noite!')
else:
    print('Turno invalido! ')
