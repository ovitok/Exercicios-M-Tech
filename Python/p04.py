# Calculadora Simples
'''def calculadora():
    
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    equaçao = input("Escolha a operação [+, -, *, /]: ")

    divisao = (n1/n2)

    multi = (n1*n2)
 
    sub = (n1-n2)

    soma = (n1+n2)

    if equaçao == "+":
        print("Seu resultado de soma deu:",soma)
    elif equaçao == "-":
        print("Sua subtração deu:",sub)
    elif equaçao == "*":
        print("Sua multiplicação deu:",multi)
    elif equaçao == "/":
        print("Sua divisão deu:",divisao)
        return
print(calculadora())'''

def calculadora2():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    equa = input('Escolha a equação (+, -, *, /): ')
    
    if equa == '+':
        resultado = (n1+n2)
    elif equa == '-':
        resultado = (n1-n2)
    elif equa == '*':
        resultado = (n1*n2)
    elif equa == '/':
        if n2 != 0:
            resultado = (n1/n2)
        else: 
            return "ERRO! NÃO PODE SER DIVIDO POR 0!"
    else:
        return "Operação inválida. Digite apenas (+,-,*,/)"
    return f"O resultado {n1}{equa}{n2} é {resultado}"
print(calculadora2())



