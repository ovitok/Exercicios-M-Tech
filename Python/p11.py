# Calculadora  de IMC

peso = float(input("Quantos kg você está pesando? "))
altura = float(input("Qual sua altura? "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Você está abaixo do peso, seu imc é {imc:.2f}")

elif  18.5 <= imc <= 24.9:
    print(f"Você está com o peso normal, seu imc é {imc:.2f}!")
elif 25 <= imc <= 29.9:
    print(f"Você está acima do peso, seu imc é {imc:.2f}!")

else:
    print(f"Você está obeso, seu imc é {imc:.2f}!")




   