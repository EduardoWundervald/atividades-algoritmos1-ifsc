# 6 - Função que conta vogais em uma string.

def contar_vogais(texto):
    if not isinstance(texto, str):
        raise TypeError("O argumento deve ser uma string.")
    vogais = set("aeiouAEIOU")
    return sum(1 for char in texto if char in vogais)

if __name__ == "__main__":
    exemplos = [
        "Olá mundo",
        "",
        "teste",
        "Python"
    ]
    for s in exemplos:
        print(f"A string '{s}' tem {contar_vogais(s)} vogais.")