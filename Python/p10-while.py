'''senha = input("Digite a senha: ")
if senha == "12345678":
    print("Acesso liberado!")
else:
    print("Você errou a senha, digite novamente!")
    senha = input("Digite a senha:")
    if senha == "12345678":
        print("Acesso liberado!")
    else:
        print("Você errou a senha, digite novamente!")
        senha = input("Digite a senha: ")
        if senha == "12345678":
            print("Acesso liberado!")
        else:
            print("Você ERROU A SENHA!!!")'''
senha = input("Digite a senha: ")
senhacerta = "12345678"
while senha != senhacerta:
    print("Senha incorreta, tente novamente!")
    senha = input("Digite a senha: ")
print("Acesso liberado!")
