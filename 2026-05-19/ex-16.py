N = int(input("Quantos termos quer? "))

if(N<3):
    print("São necessário 3 ou mais termos")
else:
    t1 = int(input("Informe o primeiro termo: "))
    t2 = int(input("Informe o segundo termo: "))
    soma_total = 0
    penultimo = t1
    ultimo = t2

    for i in range (N):
        print(penultimo)
        soma_total += penultimo
        proximo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo

    print(f"Soma dos termos: {soma_total}")