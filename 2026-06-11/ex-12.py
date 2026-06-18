#12 - Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

print(celsius_para_fahrenheit(0))
print(celsius_para_fahrenheit(100))
print(celsius_para_fahrenheit(-40))

# Chamada simples:
valor = 0
print(celsius_para_fahrenheit(valor))