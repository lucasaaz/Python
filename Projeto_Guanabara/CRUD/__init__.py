# Importações
from time import sleep
from Projeto_Guanabara.interface import*


diretorio = 'Dados.txt'

# Funções
def cadastro(opcao):
    try:
        titulo(opcao)
        arq = open(diretorio, "a+")
        while True:
            nome = str(input(' Nome: '))
            n = nome.replace(" ", "-")
            break
        while True:
            idade = str(input(' Idade: '))
            avaliar = idade.isnumeric()
            if avaliar:
                break
            print(' Erro!! Você deve digitar uma idade.')
        while True:
            sexo = str(input(' Sexo: ').strip().upper()[0])
            avaliar = sexo.isalpha()
            if avaliar and sexo in 'FM':
                break
            print(' Erro!! Você deve digitar um sexo.')
        arq.write('\n' + n + ' ')
        arq.write(idade + ' ')
        arq.write(sexo)
    except:
        sleep(1)
        print(' ERRO!! \n Não foi possivel fazer o cadastro.')
    finally:
        sleep(2)
        print(f'\n Olá {nome}, você foi cadastrado com sucesso!')
        arq.close()


def pesquisar(opcao):
    try:
        titulo(opcao)
        nome = str(input(' Digite o nome para a busca: '))
        n = nome.replace(" ", "-")
        verificar = True
        arq = open(diretorio, 'r')
        print(f' {"Nome":<15}{"Idade":^7}{"Sexo":>6}')
        for linha in arq:
            linha = linha.strip().split()
            if linha[0] == n:
                print(f' {nome:<15}{linha[1]:^5}{linha[2]:>5}     [Ok]')
                verificar = False
        if verificar:
            print(f' {"-":<15}{"-":^5}{"-":>5}')
            print(f' {nome} não foi cadastrado.')
    except Exception:
        sleep(1)
        print(' ERRO!! \n Não foi possivel fazer a pesquisa.')
    finally:
        sleep(1)
        arq.close()


def mostrarTodos(opcao):
    try:
        titulo(opcao)
        arq = open(diretorio, 'r')
        print(f' {"Nome":<15}{"Idade":^7}{"Sexo":>6}')
        lista = {}
        for linha in arq:
            linha = linha.strip().split()
            lista['nome'] = linha[0].replace("-", " ")
            lista['idade'] = linha[1]
            lista['sexo'] = linha[2]
            print(f' {lista["nome"]:<15}{lista["idade"]:^5}{lista["sexo"]:>5}')
    except Exception:
        sleep(1)
        print(' ERRO!! \n Não foi possivel mostra todos os cadastrados.')
    finally:
        sleep(1)
        arq.close()


def deletar(opcao):
    try:
        titulo(opcao)
        nome = str(input(' Digite o nome para a deletar: '))
        n = nome.replace(" ", "-")

        # Colocar as palavras em uma lista
        palavra = []
        arq = open(diretorio, 'r')
        for linha in arq:
            linha = linha.strip().split()
            palavra.append(linha)

        # Alterar lista
        verificar = True
        for linha in palavra:
            if n in linha:
                linha[0] = '*'
                verificar = False
                print(f'\n {nome} foi excluido com sucesso!')
        if verificar:
            print(f' {"Nome":<15}{"Idade":^7}{"Sexo":>6}')
            print(f' {"-":<15}{"-":^5}{"-":>5}')
            print(f' {nome} não existe.')
        arq.close()

        # Escrever no arquivo
        arquivo = open(diretorio, 'w+')
        for l in palavra:
            arquivo.write(l[0] + ' ')
            arquivo.write(l[1] + ' ')
            arquivo.write(l[2] + '\n')

    except Exception:
        sleep(1)
        print(f' ERRO!! \n Não foi possivel deletar.')
    finally:
        arquivo.close()
