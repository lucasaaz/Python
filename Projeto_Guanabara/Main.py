# Importaçoes
from interface import *

# Programa Principal
sair = True
while sair == True:
    opcao = iniciar()
    analisarOpcao(opcao)
    verificar = continuar()
    if verificar == 'N':
        sair = False
        sleep(0.5)
        print(' .', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.  ')
        sleep(0.5)
        print('\n Programa Finalizado!   ')
