# O caminho do arquivo a ser lido
file_path = "C:/Users/Riva Investimentos/Documents/Python/arquivo/texto.txt"

# Escrever no que ja ta escrito no arquivo
'''arquivo = open(file_path, "a")
arquivo.write('\nVamos nessaaa!')'''

# Colocar as palavras em uma lista
palavra = []
for linha in open(file_path, 'r'):
    linha = linha.strip()
    palavra.append(linha)
print(palavra[0])


# Abrir o arquivo em modo de leitura
with open(file_path, "r") as file:
    # Ler o conteúdo do arquivo e armazená-lo em uma variável
    file_content = file.read()
    # Imprimir o conteúdo do arquivo
    print(file_content)

# Abrir o arquivo em modo de leitura
with open(file_path, "r") as file:
    # Ler o conteúdo do arquivo da primeira linha e armazená-lo em uma variável
    file_content_linha = file.readline()
    # Imprimir o conteúdo do arquivo da primeira linha
    print(file_content_linha)

# fechando o arquivo
#arquivo.close()