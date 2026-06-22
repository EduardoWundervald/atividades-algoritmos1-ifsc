# 8 - Função que converte número para palavras (ex: 123 "cento e vinte e três").
def numero_para_palavras(n):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if n == 0: return "zero"
    if n == 100: return "cem"

    def converter_ate_999(num):
        c = num // 100
        d = (num % 100) // 10
        u = num % 10
        partes = []
        if c > 0: partes.append(centenas[c])
        if d == 1:
            partes.append(especiais[u])
        else:
            if d > 1: partes.append(dezenas[d])
            if u > 0: partes.append(unidades[u])
        return " e ".join(p for p in partes if p)

    if n < 1000:
        return converter_ate_999(n)
    else:
        mil = n // 1000
        resto = n % 1000
        parte_mil = "mil" if mil == 1 else f"{converter_ate_999(mil)} mil"
        if resto == 0:
            return parte_mil
        return f"{parte_mil} e {converter_ate_999(resto)}"

print("\n8. Número para palavras:")
print(" 123:", numero_para_palavras(123))
print(" 2023:", numero_para_palavras(2023))