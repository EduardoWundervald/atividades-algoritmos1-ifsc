def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

b = float(input("Informe a base do triângulo: "))
h = float(input("Informe a altura do triângulo: "))
resultado = calcular_area_triangulo(b, h)

print(f"A área do triângulo é: {resultado}")