# 4 - Função que codifica string em Cifra de César.
def cifra_cesar(texto, deslocamento):
    resultado = []
    for char in texto:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            novo_char = chr((ord(char) - ord(base) + deslocamento) % 26 + ord(base))
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return ''.join(resultado)

print("\n4. Cifra de César:")
print(" 'ABC' + 3:", cifra_cesar("ABC", 3))
print(" 'XYZ' + 5:", cifra_cesar("XYZ", 5))