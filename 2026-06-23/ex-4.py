# 4 - Finally em Operação de Arquivo. Crie uma função que abre um arquivo, 
# escreve "Hello World" e fecha com finally. Trate FileNotFoundError.
def escrever_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'w')
        arquivo.write("Hello World")
    except FileNotFoundError:
        print("Erro: Caminho inválido!")
    finally:
        if 'arquivo' in locals():
            arquivo.close()

# Teste:
escrever_arquivo("teste.txt")