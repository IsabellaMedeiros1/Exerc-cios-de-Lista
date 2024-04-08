'''
faça um programa que peça ao usuaria informar
quantos nomes devem ser armazenados, e em seguida deve pedir os mome e guarda-los em uma lista
'''
lista = []
quantidade = int(input("Digite quantos nomes devem ser armazenados: "))

for i in range(0, quantidade):
    print("Digite um nome: ")
    nome = input()
    lista.append(nome)
print("Lista: ", lista)
