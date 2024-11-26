# Senha com While e Break
senha_certa = "123456"
tentativas = 0
print("Sistema de Senha, você tem 3 tentativas!")
while tentativas < 3:
    senha_usuario = input("Digite a senha: ")

    if senha_usuario == senha_certa:
        print("Você acertou a senha!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! você já tentou: {tentativas}")
    if tentativas == 3:
        print("Acesso bloqueado!")



    