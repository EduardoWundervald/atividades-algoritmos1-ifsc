N = int(input("Quantos termos quer? "))
penultimo = 0
ultimo = 1

for i in range (N):
    proximo = penultimo + ultimo
    penultimo = ultimo
    ultimo = proximo
    print(proximo)

