#8 - Função que calcula o IMC (peso / altura²)
def imc(peso, altura):
    return peso / (altura ** 2)

peso = 85.0
altura = 1.77
print(imc(peso, altura))