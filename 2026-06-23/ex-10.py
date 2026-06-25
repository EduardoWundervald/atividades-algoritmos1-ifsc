# 10 - Gerenciador de Contexto. Crie um gerenciador de contexto 
# que abre arquivo e trata FileNotFoundError.
class GerenciadorArquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __enter__(self):
        try:
            self.arquivo = open(self.nome_arquivo, 'r')
            return self.arquivo
        except FileNotFoundError:
            print("Arquivo não encontrado!")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'arquivo') and self.arquivo:
            self.arquivo.close()

with GerenciadorArquivo("dados.txt") as arquivo:
    if arquivo:
        print(arquivo.read())