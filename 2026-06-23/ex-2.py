# 2 - Acesso a Lista. Escreva uma função que recebe uma lista e um índice, 
# e retorna o elemento correspondente. Trate erros de índice.
def acessar_lista(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: Índice fora do intervalo!"
    except TypeError:
        return "Erro: Índice inválido!"

# Teste:
print(acessar_lista([10, 20, 30], 1)) # 20
print(acessar_lista([10, 20, 30], 5)) # Erro