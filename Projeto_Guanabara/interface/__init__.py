# Importações
from time import sleep
from Projeto_Guanabara.CRUD import*


# Funções
def iniciar():
    try:
        print(f'\n{"="*10:<}{"Sistema":^9}{"="*10:>}')
        print(' [1] Cadastro \n [2] Pesquisar \n [3] Mostar Todos \n [4] Deletar \n [5] Fechar ')
        while True:
            opcao = int(input(' Escolha uma opção: '))
            if opcao > 0 and opcao < 6:
                break
        return opcao
    except:
        print(' ERRO!! \n Você não digitou o número certo')


def analisarOpcao(opcao):
    try:
        while True:
            if opcao == 1:
                sleep(1)
                cadastro(opcao)
                break
            elif opcao == 2:
                pesquisar(opcao)
                break
            elif opcao == 3:
                sleep(1)
                mostrarTodos(opcao)
                break
            elif opcao == 4:
                sleep(1)
                deletar(opcao)
                break
            elif opcao == 5:
                print(' ...')
                break
            else:
                break
    except Exception:
        print('')


def continuar():
    try:
        while True:
            opcao = str(input(' Deseja continuar [S][N]: ')).upper()[0]
            if opcao in 'SN':
                break
            else:
                print(' Erro!! Você deve digitar S ou N.')
        return opcao
    except:
        print(' Erro!! \n Você deve digitar S ou N.')


def titulo(opcao):
    try:
        if opcao == 1:
            print(f'\n {"="*10:<} {"Cadastro":^10} {"="*10:>} ')
        elif opcao == 2:
            print(f'\n {"="*10:<} {"Pesquisar":^11} {"="*10:>} ')
        elif opcao == 3:
            print(f'\n {"="*8:<} {"Mostrar Todos":^15} {"="*8:>} ')
        elif opcao == 4:
            print(f'\n {"="*10:<} {"Deletar":^9} {"="*10:>} ')
        elif opcao == 5:
            print(f'\n {"="*10:<} {"Fechando":^10} {"="*10:>} ')
    except:
        print(' ERRO!! \n Algo errado no Título')
