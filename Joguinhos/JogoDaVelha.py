# Jogo da Velha

tabuleiro = ["_"] * 9
vencedor = None
jogador_atual = "X"

def imprimir_tabuleiro():
    for i in range(3):
        print("|".join(tabuleiro[i*3:i*3+3]))
        print()

def jogada_valida(posicao):
    return tabuleiro[posicao] == "_"

def jogar(posicao):
    global jogador_atual
    tabuleiro[posicao] = jogador_atual0
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"

def verificar_vencedor():
    linhas = [tabuleiro[i:i+3] for i in range(0, 9, 3)]
    colunas = [tabuleiro[i:9:3] for i in range(3)]
    diagonais = [tabuleiro[0:9:4], tabuleiro[2:7:2]]
    global vencedor
    for linha in linhas + colunas + diagonais:
        if linha.count("X") == 3:
            vencedor = "X"
            return
        elif linha.count("O") == 3:
            vencedor = "O"
            return
    if "_" not in tabuleiro:
        vencedor = "Empate"
        return

while not vencedor:
    imprimir_tabuleiro()
    posicao = int(input("Jogador " + jogador_atual + ", escolha uma posição (0-8): "))
    if jogada_valida(posicao):
        jogar(posicao)
        verificar_vencedor()
    else:
        print("Jogada inválida. Escolha uma posição vazia.")

if vencedor == "Empate":
    print("Empate!")
else:
    print("Jogador " + vencedor + " venceu!")