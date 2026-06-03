n = [0]*10
x = 0

while x < len(n):
    n[x] = int(input(f"Informe o valor da posição {x} do vetor"))
    x+=1

n.reverse()
print(n)