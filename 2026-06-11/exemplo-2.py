def area_quadrado(lado):
    area = lado * lado
    return area

lado= float(input("Informe o lado do quadrado: "))
resultado = area_quadrado(lado)

print(f"A área do quadrado é: {resultado}")
