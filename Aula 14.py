from ctypes.wintypes import RECTL

nome = input("Informe seu nome:")
idade = input("Informe sua idade:")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá sou {self.nome} e tenho {self.idade} anos de idade!")

    class Veiculo:
        def __init__(self, marca: str, modelo: str, ano: int, cor: str):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano
            self.cor = cor

        def ligarMotor(self):
            print(f"Ligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

        def desligarMotor(self):
            print(f"Desligando motor de: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

    meuCarro = Carro("Toyota", "Corolla", 2020, "Prata")

    meuCarro.ligarMotor()

    carroDoAmigo = Carro("Honda", "Civic", 2019, "Preto")
    carroDoAmigo.ligarMotor()

    class Carro(Veiculo):
        def __init__(self, marca: str, modelo: str, ano: int, cor: str, num_portas: int):
            super().__init__(marca, modelo, ano, cor) #Chama o contrutor da superclasse
            self.num_portas = num_portas

        def abrir_porta_malas(self):
             print(f"O porta malas do carro {self.marca} está abrindo!")

    class Moto(Veiculo):
        def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: int):
            super().__init__(marca, modelo, ano, cor)  # Chama o contrutor da superclasse
            self.cilidadas = cilindradas

        def empinar(self):
            print(f"A {self.modelo} está empinando!")


#ENCAPSULAMENTO

class Conta:
    def __init__(self, titular, saldo = 0):
        self.titular = titula
        self.saldo = saldo # Atributo privado

    def depositar(self, quantia):
        self.saldo += quantia
    def sacar(self, quantia):
        if self.saldo <= quantia:
            self.saldo -= quantia
            return True
        else:
             return False

    def get_saldo(self):
        return self.saldo


#POLIFORMISMO: Alterar existente
