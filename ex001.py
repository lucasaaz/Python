#Manipulando Str(String)
#nome = str(input('Qual seu nome: '))
#print('Prazer em te conhecer {:<10}!'.format(nome))

#Manipulando Texto
frase = ' Curso em Video Python '
print(frase)
print(frase[10:15])
print("""Traduzido do inglês-Python é uma linguagem de programação de alto nível e de uso geral. 
Sua filosofia de design enfatiza a legibilidade do código com o uso de recuo significativo. 
Python é tipado dinamicamente e coletado como lixo.""")
print(frase.count('o'))                     #Contar quantidade de letra
print(len(frase))                           #Tamanho da frase
print(len(frase.strip()))                   #Revomer os space desnecessario
print(frase.replace('Python', 'Android'))   #Trocar palavras
print('Curso' in frase)                     #Ver se palavra esta na frase
print(frase.find('Video'))                  #Mostra a posicao da palavra
print(frase.split())                        #Cria uma Lista com as palavras