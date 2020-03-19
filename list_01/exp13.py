'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo=int(input('Escolha: \n1-Feminino \n2-Masculino\n'))

if sexo == 1:
    altura=float(input('Qual sua altura?\n'))
    peso1=(62.1*altura)-44.7
    print('Seu peso ideal é: {:.2f}' .format(peso1))
else:
    altura=float(input('Qual sua altura?\n'))
    peso2=(72.7*altura)-58
    print('seu peso ideal é: {:.2f} '.format(peso2))
         

         
