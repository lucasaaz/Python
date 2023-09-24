lista = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota: "))
    nota2 = float(input("Nota: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    var = 1
    while var == 1:
        resp = str(input("Deseja continuar? (S/N)"))
        if resp.upper()[0] not in "SN":
            print('Erro!!')
        else:
            var = 0
    if resp.upper()[0] in "N":
        break

print('-=' * 20)
print(f'{"NO.":<5} {"NOME":<10} {"MÉDIA":<5}')
print('-=' * 20)
for i, e in enumerate(lista):
    print(f'{i:<5} {e[0]:<10} {e[2]:<5.1f}')
print('-=' * 20)
while True:
    num = int(input('Mostar notas de qual aluno? (999)'))
    if num == 999:
        break
    print(f'Notas de {lista[num][0]} são {lista[num][1]}')
print('\nFechando...')