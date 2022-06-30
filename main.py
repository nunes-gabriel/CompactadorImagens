from PIL import Image
import os

# Alguns parâmetros para se definir:

# Pasta de origem de onde serão retiradas as imagens.
pasta_input = "input/"

# Pasta de origem de onde serão retiradas as imagens.
pasta_output = "output/"

# Novo tamanho das imagens compactadas em kilobytes(kb).
novo_tamanho = 50

# Fator de diminuição dos pixels, quanto menor for, mais preciso
# será o tamanho de saída dos arquivos, porém, mais lento será a
# execução do código.
fator = 50

for nome_arquivo in os.listdir(pasta_input):
    atual_tamanho = os.stat(pasta_input + nome_arquivo).st_size / 1024
    if atual_tamanho > novo_tamanho:
        try:
            imagem = Image.open(pasta_input + nome_arquivo)
            imagem_copia = imagem.copy()
            nome, formato = os.path.splitext(nome_arquivo)
            nome_copia = nome + "_copia" + formato
            while atual_tamanho > novo_tamanho - 10: # Margem de erro de 10kb.
                x, y = imagem_copia.size
                imagem_copia.thumbnail((x - fator, y - fator))
                imagem_copia.save(pasta_output + nome_copia)
                atual_tamanho = os.stat(pasta_output + nome_copia).st_size / 1024
            else:
                os.remove(pasta_output + nome_copia)
                imagem = imagem.resize((x, y))
                imagem.save(pasta_output + nome_arquivo)
        except OSError:
            print(f"{nome_arquivo} não pode ser aberto.")
    else:
        print(f"{nome_arquivo} já tem menos que {novo_tamanho}kb...")
