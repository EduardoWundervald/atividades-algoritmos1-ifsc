import math

a = int(input("Informe o valor do primeiro lado do triângulo: "))
b = int(input("Informe o valor do segundo lado do triângulo: "))
c = int(input("Informe o valor do terceiro lado do triângulo: "))

if(a+b>c and a+c>b and b+c>a):
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"É possível formar um triângulo, área: {area}")
else:
    print("Não é possível formar um triângulo")