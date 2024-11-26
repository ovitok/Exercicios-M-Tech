# Bom dia boa tarde boa noite

nome = input('Olá, qual seu nome? ')
hora = int(input('Que horas são aí? '))
if 6 <= hora < 12:
    print('Bom dia,',nome)
elif 12 <= hora < 18:
    print('Boa tarde,',nome)
else:
    print('Boa noite,',nome)





