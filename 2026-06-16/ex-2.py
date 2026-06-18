 # 2 - Função que verifica se uma string é palíndromo.
def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

print("\n2. 'Radar' é palindromo?", eh_palindromo("Radar"))
print(" 'Python' é palindromo?", eh_palindromo("Python"))
print(" 'A base do teto desaba' é palindromo?", eh_palindromo("A base do teto desaba"))