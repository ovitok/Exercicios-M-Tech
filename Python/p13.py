import random
# Pedra Papel Tesoura
sua_escolha = input("Escolha entre Pedra, Papel e Tesoura: ").lower()
jogo = ("Pedra","Papel","Tesoura")
pc = random.choice(jogo)

if pc == "Pedra" and sua_escolha == "Papel":
    print(f"Você ganou! O computador escolheu:{pc}")
elif pc == "Pedra"and sua_escolha == "Tesoura":
    print(f"Você perdeu! O computador escolheu:{pc}")
elif pc == "Pedra" and sua_escolha == "Pedra":
    print(f"Empatou! O computador escolheu:{pc}")
elif pc == "Papel" and sua_escolha == "Pedra":
    print(f"Você perdeu! O computador escolheu:{pc}")
elif pc == "Papel"and sua_escolha == "Tesoura":
    print(f"Você ganhou! O computador escolheu:{pc}")





          
        