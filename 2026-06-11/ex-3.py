# 3 - Função que concatena duas strings.

def concatenar_strings(string1, string2):
    return string1 + string2

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
resultado = concatenar_strings(string1, string2)
print(f"A concatenação das strings é: {resultado}.")