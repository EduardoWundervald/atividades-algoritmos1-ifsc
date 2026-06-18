# 9 - Função que verifica se todos os elementos são pares.
def todos_pares(lista):
    for num in lista:
        if num % 2 != 0:
            return False
    return True

print("\n9. Todos pares [2,4,6,8]?", todos_pares([2,4,6,8]))
print(" Todos pares [2,4,5,8]?", todos_pares([2,4,5,8]))