dicionario = dict()
lista = list()
soma = media = 0
while True:
    dicionario['nome'] = str(input('Qual seu nome: '))
    while True:
        dicionario['sexo'] = str(input('Qual seu sexo: (M/F) ')).upper()[0]
        if dicionario['sexo'] in 'MF':
            break
        print('Erro!!\n')
    dicionario['idade'] = int(input('Qual sua idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    dicionario.clear()
    while True:
        resp = str(input("Deseja continuar: (S/N)")).upper()[0]
        if resp in 'SN':
            break
        print('Erro!!\n')
    if resp in 'N':
        break
print(' -='*15)
print(f' O número de pessoa cadastradas é {len(lista)}')
media = soma / len(lista)
print(f'\n A media das idades é {media:.2f}\n')
for i, e in enumerate(lista):
    if e['sexo'] in 'F':
        print(f' {i + 1}° pessoa é a mulher {e["nome"]}')
print()
for i, e in enumerate(lista):
    if e['idade'] > media:
        print(f' {e["nome"]} com {e["idade"]} anos, tem idade acima da media de {media} anos')

