lista = []
for i in range (5):
    num = int(input(f"Informe o número {i+1} de 5: "))
    lista.append(num)

del lista [0]
novo = int(input("Digite novo número: "))
lista.append(novo)

print("Nova lista:", lista)