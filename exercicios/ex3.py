'''
com base na lista a seguir:
[1, 2 , 3 , 4  , 5, 6 ,7 , 8, 9, 10, 11, 12]

faça um cod que remova todos os numeros desta lista que são divisiveis por 3

'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista_divisao = [i for i in lista if i % 3]

print(lista_divisao)