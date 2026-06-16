# 2 - Função que verifica se um número é positivo.

def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se é positivo: "))
resultado = positivo(numero)
print(f"O número {numero} é positivo? {resultado}.")