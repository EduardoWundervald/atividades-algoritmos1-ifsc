a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))
i = 1
numeros = [a,b,c]
ordenados = sorted(numeros)
ordenados_decrescente = sorted(numeros, reverse=True)

while(i!=0):
    i = int(input("Digite a opção desejada: "))
    match i:
        case 1: 
            print(f"Ordem crescente: {ordenados[0]}, {ordenados[1]}, {ordenados[2]}")
        case 2:
            print(f"Ordem decrescente: {ordenados_decrescente[0]}, {ordenados_decrescente[1]}, {ordenados_decrescente[2]}")
        case 3: 
            print(f"Com o maior número no centro: {ordenados[0]}, {ordenados[2]}, {ordenados[1]}")
        case _:
            print("Opção inválida")


