import random as rd

class Personagem:
    def __init__(self, nome: str, vida: int, defesa: int, ataque: int ):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        dano = max(self.ataque - self.defesa, 0) #o dano não vai ser um número negativo, feito para a opção de defesa
        alvo.vida -= dano
        return dano

    def fortalecer(self, valor = 2):
        self.ataque += valor
        return valor

    def curar(self, valor = 10):
        self.vida = min(self.vida+valor,100)
        return self

class JogoRPG:
    def __init__(self, ):
        nome_player = input("Qual seu nome?")
        self.player = Personagem(nome_player, vida = 100,defesa=10, ataque=10)
        self.inimigo = Personagem(nome="Boss", vida=100,defesa=9, ataque=15)

    def iniciar(self):
        print(f"Batalha entre {self.player.nome} e {self.inimigo.nome}!")
        while self.player.esta_vivo() and self.inimigo.esta_vivo():
            self.turno_jogador()
            self.turno_inimigo()
        self.finalizar_jogo()

    def turno_jogador(self):
        print(f"{self.player.nome}: {self.player.vida} HP | {self.inimigo.nome}: {self.inimigo.vida} HP ")
        escolha = input("Ação: [1] Atacar | [2] Fortalecer | [3] Curar: \n")
        if escolha == "1":
            dano = self.player.atacar(self.inimigo)
            print(f"{self.player.nome} atacou {self.inimigo.nome} causando {dano} de dano")
        elif escolha == "2":
            valor_do_dado = self.player.fortalecer(rd.randint(1, 5))
            self.player.fortalecer(valor_do_dado)
            print(f"{self.player.nome} aumentou seu ataque em {valor_do_dado}!")
        elif escolha == "3":
            valor_cura = rd.randint(1, 5)
            self.player.curar(valor_cura)
            print(f"{self.player.nome} aumentou sua vida em {valor_cura}!")
        else:
            print("Escolha um valor válido")

    def turno_inimigo(self):
          acao = rd.choice(["atacar", "fortalecer", "curar"])
          match acao:
             case 'atacar':
                  dano = self.inimigo.atacar(self.player)
                  print(f" {self.inimigo.nome}catacou {self.player.nome} causando {dano} de dano")

             case 'fortalecer':
                 valor_do_dado = self.player.fortalecer(rd.randint(1, 5))
                 self.player.fortalecer(valor_do_dado)
                 print(f"{self.player.nome} aumentou seu ataque em {valor_do_dado}!")

             case 'curar':
                 valor_cura = rd.randint(1, 5)
                 self.player.curar(valor_cura)
                 print(f"{self.inimigo.nome} aumentou sua vida em {valor_cura}!")

    def finalizar_jogo(self):
        print(f"{self.player.nome} perdeu!") if not self.player.esta_vivo() else print(f"Parabéns, {self.player.nome}, você venceu!")

if __name__ == '__main__':
     jogo = JogoRPG()
     jogo.iniciar()