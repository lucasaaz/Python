# programa para ler um arquivo e escrever o conteúdo

# escrever no arquivo
arquivo = open('texto.txt', 'w')
arquivo.write('\nOiii')

# abrir e modificar
arquivo = open('texto.txt', 'a')
arquivo.write('\nBora aprender Python!')

# abrindo o arquivo
arquivo = open('texto.txt', 'r')

# lendo o conteúdo do arquivo
conteudo = arquivo.read()

# imprimindo o conteúdo do arquivo
print(conteudo)

# fechando o arquivo
arquivo.close()