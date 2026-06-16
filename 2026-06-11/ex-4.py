# 4 - Função que calcula a área de um retângulo.

def area_retangulo(base, altura):
    return base * altura

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
resultado = area_retangulo(base, altura)
print(f"A área do retângulo é: {resultado}.")
