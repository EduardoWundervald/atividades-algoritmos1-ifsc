# 9 - Função que calcula determinante de matriz 3x3.
def determinante_3x3(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

print("\n9. Determinante matriz 3x3:")
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(" Determinante:", determinante_3x3(mat))