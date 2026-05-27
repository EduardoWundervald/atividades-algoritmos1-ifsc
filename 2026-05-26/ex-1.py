n = 0
maior = 0
while n < 10:
    n += 1
    a = int(input("Informe um número: "))
    if(a>maior):
        maior = a

print(f"O maior número é {maior}")