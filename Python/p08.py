# Classificação de Idade

idade = int(input('Qual sua idade? '))
if idade <= 12:
    print("Você é criança!")
elif idade <= 17:
    print("Você é adolescente!")
elif idade <= 64:
    print("Você é adulto!")
else:
    print("Você é idoso!")


