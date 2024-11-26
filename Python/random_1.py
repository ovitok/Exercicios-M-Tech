'''import random
numero = random.randint(333,777)
print(numero)'''

def contagem_regressiva():
    tempo_inicial = int(input("Digite um número para iniciar a contagem regressiva: "))

    while tempo_inicial >= 0:
        print(tempo_inicial)

        if input ("") == "parar":
            print("Contagem regressiva interrompida")
        break

    tempo_inicial -= 1

    if tempo_inicial < 0:
        print("Contagem regressiva concluída!")
print(contagem_regressiva())
