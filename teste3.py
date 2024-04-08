try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    resultado = n1/n2
    print(f"O resultado é {resultado}")
except ValueError as err:
    print("Digite um número válido")
except ZeroDivisionError as err:
    print("Informe um número difente de 0")
except:
    print("Não é possível fazer a conta")