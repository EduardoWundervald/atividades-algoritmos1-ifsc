n = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    n[x] = float(input(f"Digite a nota {x+1}: "))
    x += 1
x = 0
x = int(input("Informe a posição que deseja acessar de 1 a 5: "))
print(f"Posição {x}: {n[x-1]}")