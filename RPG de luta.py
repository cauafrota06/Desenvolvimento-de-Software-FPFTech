import random

jogador1 = input("Informe o nome do jogador 1: ")
jogador2 = input("Informe o nome do jogador 2: ")

vidaJogador1 = 100
vidaJogador2 = 100
forcaJogador1 = 20
forcaJogador2 = 20

quemInicia = random.randint(1, 2)
turno_atual = quemInicia

def ataque1():
    global vidaJogador2
    vidaJogador2 = vidaJogador2 - forcaJogador1

def ataque2():
    global vidaJogador1
    vidaJogador1 = vidaJogador1 - forcaJogador2

print(f"\nO sorteio decidiu: Jogador {quemInicia} inicia!")

while vidaJogador1 > 0 and vidaJogador2 > 0:
    print("-" * 40)
    print(f"VIDA: {jogador1} [{vidaJogador1}] | {jogador2} [{vidaJogador2}]")

    if turno_atual == 1:
        print(f"\n> Turno {jogador1}")
        print("1. Ataque | 2. Cura | 3. Sair")
        escolhajogador = input("Escolha sua ação: ")

        if escolhajogador == "1":
            ataque1()
            print(f"SUCESSO: {jogador1} atacou {jogador2}!")
        elif escolhajogador == "2":
            cura = 5
            vidaJogador1 += cura
            print(f"RECUPERAÇÃO: {jogador1} curou {cura} de vida!")
        elif escolhajogador == "3":
            print(f"{jogador1} fugiu da batalha!")
            break
        else:
            print("Opção inválida! Você perdeu o turno.")

        turno_atual = 2

    else:
        print(f"\n> Turno {jogador2} (Oponente)")
        escolhaOponente = random.randint(1, 2)

        if escolhaOponente == 1:
            ataque2()
            print(f"{jogador2} atacou!")
        else:
            vidaJogador2 += 5
            print(f"{jogador2} se curou!")

        turno_atual = 1

print("\n" + "=" * 30)
print("       === FIM DE JOGO ===       ")
if vidaJogador1 <= 0:
    print(f"O vencedor é {jogador2}!")
elif vidaJogador2 <= 0:
    print(f"O vencedor é {jogador1}!")





