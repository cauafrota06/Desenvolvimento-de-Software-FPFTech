# Funções com Argumentos nomeados x Argumentos posicionais

#Função com argumentos posicionais
 #Toda a função em python começa com um 'def'

def somarPosicional(num1, num2):
    print(f'O primeiro numero tem valor: {num1}')
    print(f'O segundo numero tem valor: {num2}')
    return num1 + num2

print(somarPosicional(4,8))  #Chamada da função, já definindo o valor das variáveis

print("\n")
#Função com argumentos nomeados

def expNomeado(num1=1, num2=1):
    print(f'O primeiro numero tem valor: {num1}')
    print(f'O segundo numero tem valor: {num2}')
    return num1 ** num2

# print(expNomeado(num2 = 8, num1 = 4)) #Aqui no argumento nomeado a posição das variáveis pode mudar, como neste exemplo
print(expNomeado(num1=5))

print("\n")
#print() com argumentos nomeados

print("print() com argumentos nomeados")
num1 = 10
num2 = 20
print(num1, num2, sep='-',end="\n")
print("\n")
#F string
print(f'num 1 é {num1} | num 2 é {num2}')
print("num1 é {}  | num2 é {}".format(num1, num2))
print("num1 é {n1} | num2 é {n2}".format(n2=num2,n1=num1))
print("\n")
#Operações aritméticas
print(f'Adição: {num1+num2}')
print(f'Subtração: {num1-num2}')
print(f'Multiplicação: {num1*num2}')
print(f'Divisão: {num1/num2}')
print(f'Divisão: {num1//num2}') #Divisão inteira #resultado 2 = inteiro
print(f'Divisão: {num1/num2}')
print(f'Exponencial: {num1**num2}')
print("\n")
#Operações Relacionais
print(f'Maior que: {num1>num2}')
print(f'Maior ou igual que: {num1>=num2}')
print(f'Menor que: {num1>num2}')
print(f'Menor ou igual que: {num1<=num2}')
print(f'É igual a: {num1==num2}')
print(f'É igual a: {num1!=num2}')

print("\n")
#Operadores Lógicos
num3 = 15

#print(f"Usando and: {num1 < num2 and num2 > num3}")
#print(f"Usando or: {num1 < num2 or num2 > num3}")

num4 = num2
num5 = 20

print(num4 is num2)
print(num5 is num2)

print("\n")
cachorro1 = ["Caramelo","Poodle", "Salsicha"]
cachorro2 = cachorro1
cachorro3 = ["Caramelo","Poodle", "Salsicha"]

print(cachorro1 is cachorro2)
print(cachorro1 is cachorro3)

