media = 0
maior = 0
soma = 0
contar = 0
nomeMaior = ''
for c in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo M/F: ')).strip()

    #Somar idades
    soma += idade

    if sexo in 'Mm':
        if idade > maior:
            maior = idade
            nomeMaior = nome
    else:
        if idade < 20:
            contar += 1
#Media
media = soma / 4
print('\nMedia das idades é: {}'.format(media))

#Nome do homem mais velho
print('Nome do Homem mais velho é: {}'.format(nomeMaior))

#Num de mulheres menores de 20 anos
print('Número de mulheres com menos de 20 anos é: {}'.format(contar))