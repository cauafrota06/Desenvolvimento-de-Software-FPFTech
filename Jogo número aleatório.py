import random

numero = random.randint(1, 100)
vidas = 6

palpite = int(input("Informe um palpite:"))

while vidas > 0:
    if palpite == numero:
        print("Parabéns! Acertou o número!")
        break
    elif (palpite > numero):
        print("O número sorteado é menor!")
    else:
        print("O número sorteado é maior!")

    vidas -= 1

    if vidas > 0:
        palpite = int(input("Informe um palpite:"))

if vidas == 0:
    print(f"O número sorteado é {numero}!")
