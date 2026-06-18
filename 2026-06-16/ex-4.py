# 4 - Função que calcula média de lista (recursivo).
def media_recursiva(lista):
    if not lista:
        return 0
    if len(lista) == 1:
        return lista[0]
    return (lista[0] + media_recursiva(lista[1:]) * (len(lista)-1)) / len(lista)

print("\n4. Média de [10, 20, 30] (recursiva):", media_recursiva([10, 20, 30]))
print(" Média de [5, 5, 5, 5]:", media_recursiva([5, 5, 5, 5]))