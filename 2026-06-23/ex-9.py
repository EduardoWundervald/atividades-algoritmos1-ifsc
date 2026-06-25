# 9 - Loop com Tratamento de Erros. Peça um índice ao usuário em 
# loop até ser válido para uma lista pré-definida.
lista = [10, 20, 30]
while True:
    try:
        indice = int(input("Índice: "))
        print(f"Elemento: {lista[indice]}")
        break
    except IndexError:
        print("Índice fora do intervalo!")
    except ValueError:
        print("Digite um número!")