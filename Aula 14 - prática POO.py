from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.__salario = salario_base

    @property
    def salario(self): # método público
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
        else:
            print("Erro, salário deve ser positivo!")
    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

class Programador(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

time_ti = [
    Gerente("Alice", 8000),
    Programador("Bob", 5000),
    Gerente("Carol", 7000),
    Programador("David", 2000)

]

print("--------------FOLHA DE PAGAMENTO----------------")

for f in time_ti:
    print(f"Funcionário: {f.nome}")
    print(f"Salário base: R${f.salario:.2f}")
    print(f"Bônus: R${f.calcular_bonus():.2f}")
    print("-" * 20)

time_ti[1].salario = 5500
print(f"Novo salário do Bob: R${time_ti[1].salario:.2f}")