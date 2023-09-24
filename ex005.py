palavra = str(input('Digite uma frase: ')).strip().upper()
frase = palavra.split()
juntar = ''.join(frase)
inverso = ''

for c in range(len(juntar) - 1, -1, -1):
     inverso += juntar[c]
     #print(juntar[c])
     #print(inverso)

if juntar == inverso:
    print('É um PALINDROMO')
    print('A palavra {} é igual ao seu inverso {}'.format(juntar, inverso))
else:
    print('Não é um PALINDROMO')
    print('A palavra {} não é igual ao seu inverso {}'.format(juntar, inverso))