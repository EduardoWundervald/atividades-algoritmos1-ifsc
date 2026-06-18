# 3 - Função que encontra o maior número em uma lista.
def maximo_lista(lista):
    if not lista:
        return None
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

print("\n3. Máximo em [3, 1, 4, 2]:", maximo_lista([3, 1, 4, 2]))
print(" Máximo em [10, 20, 5]:", maximo_lista([10, 20, 5]))
print(" Máximo em lista vazia:", maximo_lista([]))