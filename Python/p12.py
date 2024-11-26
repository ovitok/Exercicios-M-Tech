# Verificador de número primo
numero = int(input("Digite um número para saber se ele é primo: "))
cauculo = (numero / 2) and (numero / 3) and (numero / 5)
if (cauculo % 2 == 0) or (cauculo % 3 == 0) or (cauculo % 5 == 0):
    print("Seu número não é primo!")
else:
    print("Seu número é primo!")

'''numero = int(input("Digite um número: "))
if numero % 3:
    print("Seu número é primo!")
else:
    print("Seu número não é primo!")'''




