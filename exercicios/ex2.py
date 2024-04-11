'''
aproveitando o ex1, mostre a lista de nomes na orde inversa que foi digitada

'''

lista = []
quantidade = int(input("Digite quantos nomes devem ser armazenados: "))

for i in range(0, quantidade):
     print("Digite um nome: ")
     nome = input()
     lista.append(nome)
     sub_lista = lista[-1::-1]
print(sub_lista)