#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
n1=float(input('Informe a primeira nota: '))
n2=float(input('informe a segunda nota:'))
media = (n1 + n2) / 2
if media >= 9.0 or media >= 10:
    print('Notas: {} + {}\nMedia: {}\nVocê ganhou um A\nAPROVADO!'.format(n1,n2,media))
elif media >= 7.5 or media > 9.0:
    print('Notas: {} + {}\nMedia: {}\nVocê ganhou um B\nAPROVADO'.format(n1,n2,media))
elif media >= 6.0 or media > 7.5:
    print('Notas: {} + {}\nMedia: {}\nVocê ganhou um C\nAPROVADO'.format(n1,n2,media))
elif media >= 4.0 or media > 6.0:
    print('Notas: {} + {}\nMedia: {}\nVocê ganhou um D\nREPROVADO'.format(n1,n2,media))
elif media < 4.0 or media == 0:
    print('Notas: {} + {}\nMedia: {}\nVocê ganhou um E\nREPROVADO'.format(n1,n2,media))
