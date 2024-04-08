lista = ["Pedro","João", "Maria", "Pedro"]
print("Lista original: ", lista, "\n\n________________")

lista.append("José") #adicionar um valor na lista
print(lista, "\n\n________________")

tamanho = len(lista) #n total da lista
print("Tamanho", tamanho, "\n\n________________")


lista.insert(1, "Matheus") #adicionar um valor em uma determinada localização
print("Lista insert: ", lista, "\n\n________________")

tamanho = len(lista)#para att a lista novamente
print("Tamanho: ", tamanho, "\nLista: ", lista, "\n\n________________")


Pedros = lista.count("Pedro") #para mostrar quantos determinados valores tem na lista
print(f"Há {Pedros} Pedros na lista", "\n\n________________")

lista.remove("Pedro") #remover um valor da lista (sem ser de colocar a localização, numero)
print("Lista remove: ", lista, "\n\n________________")

lista.pop(2) #Remove pela posição
print("Lista sem a Maria(está na posição 3): ", lista, "\n\n________________")

