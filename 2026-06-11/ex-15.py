#15 - Função que conta caracteres não-espaço em uma string
def contar_nao_espacos(texto):
    return len(texto.replace(" ", ""))

# Chamada exemplo:
texto = "Olá Mundo"
print(contar_nao_espacos(texto))