# 7 - Else em Bloco Try. Modifique o exercício 3 para usar else: se 
# a conversão for bem-sucedida, imprima "Conversão OK".
def converter_inteiro_com_else():
    entrada = input("Digite um valor: ")
    try:
        numero = int(entrada)
    except ValueError:
        return "Erro: Valor inválido!"
    else:
        print("Conversão OK!")
        return numero

# Teste:
print(converter_inteiro_com_else())