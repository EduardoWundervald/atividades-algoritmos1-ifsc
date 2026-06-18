#10 - Função que remove espaços de uma string
def remover_espacos(texto):
    return texto.replace(" ", "")

texto = "texto com espaços"
print(remover_espacos(texto))