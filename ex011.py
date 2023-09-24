from random import randint
from time import sleep
from operator import itemgetter
dicionario = {'jogador1': randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)}
lista = []
maior = 0
print(f'    Numeros Sorteados:')
for i, e in dicionario.items():
    print(f'   O {i} tirou: {e}')
    sleep(1)
    if e > maior:
        maior = e
        jogador = i
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print(' -=' * 14, f'\n    Ranking:')
for i, e in enumerate(ranking):
    print(f'   {i+1}° lugar foi o {e[0]} que tirou {e[1]}')
print(f'\n O campeao foi o {jogador} com o numero {maior}')


