lista=["Isabella", "Guilherme", "Pablo", "Mikael", "Juliana", "Enzo", "Vincenzo", "Guilherme"]
#indice:   0           1           2        3          4         5         6           7


pos = lista.index("Pablo") #procurar uma informação dentro da lista
print(f"O Pablo está na posição {pos}", "\n\n____________________")

pos = lista.index("Guilherme", 2 ) #procurar uma informação dentro da lista a partir de uma determinada posição
print(f"O Guilherme está na posição {pos}", "\n\n____________________")


print(f"A posição -8 é {lista[-8]}", "\n\n____________________")#indice na posição negativa seria quando voltasse

try:       #tentar executar um comando, se der erro executa o except
    pos = lista.index("Mariana")
    print("Tem maria")
except ValueError as err:         #se colocar ValueError mostra q: se der um erro daquele tipo vai mostrar a mensagem
    print("Não há Mariana na lista")
    print("Erro: ", err)