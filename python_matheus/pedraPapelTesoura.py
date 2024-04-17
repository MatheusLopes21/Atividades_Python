import random

def jogo_pedra_papel_tesoura():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    while True:
        print("\nEscolha sua jogada:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        print("4. Sair do jogo")

        escolha = input("Digite o número correspondente à sua jogada: ")

        if escolha == "4":
            print("Você saiu do jogo.")
            break
        elif escolha not in ["1", "2", "3"]:
            print("Escolha inválida. Por favor, escolha novamente.")
            continue

        jogador = opcoes[int(escolha) - 1]
        computador = random.choice(opcoes)

        print("Você escolheu:", jogador)
        print("O computador escolheu:", computador)

        if jogador == computador:
            print("Empate!")
        elif (jogador == "Pedra" and computador == "Tesoura") or \
             (jogador == "Papel" and computador == "Pedra") or \
             (jogador == "Tesoura" and computador == "Papel"):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

jogo_pedra_papel_tesoura()
