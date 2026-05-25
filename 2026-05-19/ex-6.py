codigo = input("Informe o código do produto: ")
quantidade = int(input("Informe a quantidade: "))
preco = 0

if(codigo=="1001"):
    preco=5.32
elif(codigo=="1324"):
    preco=6.45
elif(codigo=="6548"):
    preco=2.37
elif(codigo=="0987"):
    preco=5.32
elif(codigo=="7623"):
    preco=6.45
else:
    print("Código inválido")

print(preco*quantidade)