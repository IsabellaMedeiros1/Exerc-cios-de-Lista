'''
com base na lista a seguir:
[1, 2 , 3 , 4  , 5, 6 ,7 , 8, 9, 10, 11, 12]

faça um cod que remova todos os numeros desta lista que são divisiveis por 3

'''


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(0, 12):
    div = lista - 3
    lista.remove(div)
print(lista)