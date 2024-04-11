''''
Faça um programa usando laços para desenhar
um  X grande na tela conforme mostrado abaixo:
*                                *
  *                            *
    *                        *
      *                    *
        *                *
          *            *
            *        *
              *    *
                **
              *    *
            *        *
          *            *
        *                *
      *                    *
    *                        *
  *                            *
*                                *
'''

tamanho = int(input("Tamanho desejado: "))

for i in range(tamanho):
    for j in range(i):
        print(" ", end="")
    print("*", end="")
    for j in range(2 * (tamanho - i - 1)):
        print(" ", end="")
    if i != tamanho - 1:
        print("*", end="")
    print()

for i in range(tamanho -2, -1, -1):
    for j in range(i):
        print(" ", end="")
    print("*", end="")
    
    for j in range(2 * (tamanho - i - 1)):
        print(" ", end="")
    if i != tamanho - 1:
        print("*", end="")
    print()
