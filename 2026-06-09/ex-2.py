pares = []
impares = []
for i in range (20):
    num = int(input(f"Informe o número {i+1} de 20: "))
    if(num%2==0):
        pares.append(num)
    else:
        impares.append(num)

print(f"Números pares:")
print(pares)
print(f"Números ímpares:")
print(impares)