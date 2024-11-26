import random
numero = random.randint(1, 10)
a = int(input('Escolha um número de 1 a 10: '))
if numero == a:
    print('Você acertou o número!')
else:
    print('Você errou :( o número era:',numero)
    

