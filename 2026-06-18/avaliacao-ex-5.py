import random

numero = random.randint(1, 50)
tentativas = 0
palpite = 0
while(palpite != numero):
    n = int(input("Informe um número entre 1 e 50: "))
    palpite = n
    tentativas += 1
    if(n > numero and n <= 50):
        print("Muito alto")
    elif(n < numero and n >= 1):
        print("Muito baixo")
    elif(n < 1 or n > 50):
        print("Número inválido, deve estar entre 1 e 50")

print(f"Parabéns, você acertou em {tentativas} tentativas!")