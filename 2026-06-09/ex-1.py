n = []
vogais = []
n_vogais = 0

for i in range (10):
    letra = str(input(f"Informe a letra da posição {i+1} do vetor: "))
    n.append(letra)

    if(n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u"):
        vogais.append(n[i])
        n_vogais+=1

for i in range (n_vogais):
    print(f"Vogais informadas:{vogais[i]}")

print(f"Quantidade de vogais: {n_vogais}")