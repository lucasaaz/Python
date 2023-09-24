listagem = ('Banana', 'Morango', 'Pessego', 'Uva', 'Melancia', 'Abacaxi',
            'Abacate', 'Amora', 'Maca', 'lixia', 'Limao', 'Laranja')
vogais = "aeiou"
for p in listagem:
    contarVogais = contarConsoates = 0;
    listaVogais = []
    listaConsoantes = []
    print(f'A palavra {p} tem ', end='')
    for letras in p:
        if letras.lower() in vogais:
            listaVogais.append(letras)
            contarVogais += 1
        else:
            listaConsoantes.append(letras)
            contarConsoates += 1
    print(f'{contarVogais} vogais sendo elas ', listaVogais, end='')
    print(f', tem {contarConsoates} consoates sendo elas ', listaConsoantes)


