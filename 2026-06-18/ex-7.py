# 7 - Função que implementa busca binária recursiva.
def busca_binaria_recursiva(lista, alvo, inicio=0, fim=None):
    fim = fim if fim is not None else len(lista) - 1
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)

print("\n7. Busca binária recursiva:")
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
print(" Posição de 7:", busca_binaria_recursiva(lista_ordenada, 7))
print(" Posição de 8:", busca_binaria_recursiva(lista_ordenada, 8))