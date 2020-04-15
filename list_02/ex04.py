#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
l=str(input('Digite uma letra: '))
if l.lower() == 'a' or l.lower() == 'e' or l.lower()=='i' or l.lower()=='o' or l.lower()=='u':
    print('{} é uma vogal'.format(l))
else:
    print('{} é consoante'.format(l))


