# 1 - Função que retorna o dobro de um número.

def dobro(numero):
    return numero * 2

numero = int(input("Digite um número para saber o dobro: "))
resultado = dobro(numero)
print(f"O dobro de {numero} é {resultado}.")