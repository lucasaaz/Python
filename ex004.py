num = int(input('Digite um numero: '))
contar = int(0)

for c in range(1, num+1):
    if num % c == 0:
        contar += 1
if contar == 2:
    print('Primo')
else:
    print('Não é Primo')