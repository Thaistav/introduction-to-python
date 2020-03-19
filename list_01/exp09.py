#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
F=float(input('Informe a temperatura em graus farenheit: '))
C=(5*(F-32)/9)
print('A temperatura em graus celsius é: {:.1f} '.format(C))
