valor = int(input("Informe o valor do saque: "))

notas_100 = valor // 100
notas_50 = (valor % 100) // 50
notas_10 = ((valor % 100) % 50) // 10
notas_5 = (((valor % 100) % 50) % 10) // 5
notas_1 = ((((valor % 100) % 50) % 10) % 5) // 1

print(f"Valor lido: {valor}")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")