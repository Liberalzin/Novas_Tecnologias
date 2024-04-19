def print_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = 0

    print("Bem-vindo ao Jogo da Velha!")

    for _ in range(9):
        print_tabuleiro(tabuleiro)
        print(f"Jogador {jogadores[jogador_atual]}, é sua vez.")

        linha = int(input("Escolha a linha (0, 1 ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogadores[jogador_atual]

        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            print_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogadores[jogador_atual]} venceu!")
            return

        jogador_atual = (jogador_atual + 1) % 2

    print_tabuleiro(tabuleiro)
    print("Empate!")

jogo_da_velha()
