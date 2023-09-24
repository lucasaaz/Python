from random import randint
from time import sleep

print('-' * 30)
print('      JOGO DA MEGA SENA   ')
print('-' * 30)

numeros = []
todos_numeros = []

numero = int(input('Quantos jogo você quer que eu sorteie?'))

for i in range(0, numero): #num de sorteios
    contar = 0
    while True:  #os num sorteados de 1 a 60
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            contar += 1
        if contar > 5:
            break
    numeros.sort()
    todos_numeros.append(numeros[:])
    numeros.clear()
print(f'\n     {numero} Numeros Sorteados  ')
for i, e in enumerate(todos_numeros):
    print(f'{i+1}° jogo: {e}')
    sleep(1)
