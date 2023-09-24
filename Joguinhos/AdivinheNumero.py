from random import randint
computador = randint(1, 100)
status = False

while not status:
    num = int(input(('\nEscolha um numero: ')))

    if num < computador:
        print('Errou!! É um número maior!!')
    elif num > computador:
        print('Errou!! É um número menor')
    else:
        print('Acertou!!')
        status = True5