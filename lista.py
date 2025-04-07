# EXERCICIO 1 

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")


# EXERCICIO 2 

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero."

print(f"\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


# calculadora de descontos

valor = float(input("Digite o valor do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))
valor_final = valor - (valor * desconto / 100)

print(f"O valor final do produto com desconto é: R$ {valor_final:.2f}")


# Adivinhe o Número

import random

numero_secreto = random.randint(1, 10)

print("Adivinhe o número entre 1 e 10!")

tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Digite seu palpite: "))
    
    if tentativa < numero_secreto:
        print("Tente um número maior!")
    elif tentativa > numero_secreto:
        print("Tente um número menor!")
    else:
        print("Parabéns! Você acertou!")


# Sistema de Controle de Acesso

senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")


# Calculadora de IMC

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")


# Contador de Números Pares

pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nNúmeros pares: {pares}")
print(f"Números ímpares: {impares}")


# Listagem de Múltiplos de 3

print("Números múltiplos de 3 entre 1 e 50:")

for numero in range(1, 51):
    if numero % 3 == 0:
        print(numero)


# Cadastro de Clientes

clientes = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º cliente: ")
    telefone = input(f"Digite o telefone do {i+1}º cliente: ")
    
    cliente = {
        "nome": nome,
        "telefone": telefone
    }
    
    clientes.append(cliente)

print("\nClientes cadastrados:")
for cliente in clientes:
    print(f"Nome: {cliente['nome']}, Telefone: {cliente['telefone']}")


# Lista de Compras Dinâmica

lista_compras = []

while True:
    item = input("Digite o item para adicionar à lista: ")
    lista_compras.append(item)
    
    continuar = input("Deseja adicionar outro item? (s/n): ").lower()
    if continuar != "s":
        break

print("\nLista de Compras:")
for item in lista_compras:
    print("-", item)


# Função de Boas-Vindas Personalizada

def boas_vindas(nome, idade):
    print(f"Bem-vindo, {nome}! Você tem {idade} anos.")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

boas_vindas(nome, idade)


# Função de Aprovação de Aluno

def verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f"Média {media:.2f} - Aprovado")
    else:
        print(f"Média {media:.2f} - Reprovado")

# Exemplo de uso
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

verificar_aprovacao(nota1, nota2)








