#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo=str(input('Informe o sexo com: "F" ou "M" '))
if sexo == 'F':
    print('Feminino')
elif sexo=='M':
    print('Masculino')
else:
    print('Sexo invalido')
    
