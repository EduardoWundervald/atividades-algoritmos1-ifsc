# 7 - Função que conta palavras em uma string.
def contar_palavras(texto):
    return len(texto.split())

print("\n7. Palavras em 'Python é incrível!':", contar_palavras("Python é incrível!"))