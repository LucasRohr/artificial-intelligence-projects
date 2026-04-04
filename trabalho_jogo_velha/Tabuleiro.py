class Tabuleiro:
    def __init__(self):
        # Matriz 3x3 para representar o tabuleiro do jogo da velha
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    # Exibe o tabuleiro de forma visual
    def exibir(self):
        print("\n")

        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)
    
    # Gera uma lista de ações possíveis (posições vazias) no tabuleiro
    # ACTIONS(state) -> list of actions
    def gerar_acoes_possiveis(self):
        acoes = []

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == ' ':
                    acoes.append((i, j))

        return acoes
    
    # Verifica possibilidade de jogada e atualiza o tabuleiro com o respectivo jogador ('X' ou 'O')
    # RESULT(state, action) -> new_state
    def fazer_jogada(self, posicao, jogador):
        i, j = posicao

        is_posicao_invalida = i < 1 or i > 3 or j < 1 or j > 3

        if is_posicao_invalida:
            return False  # Posição inválida

        if self.tabuleiro[i - 1][j - 1] == ' ':
            self.tabuleiro[i - 1][j - 1] = jogador
            return True
        
        return False
    
    # Checa por vencedor da partida
    # TERMINAL(state) -> boolean
    def verificar_vencedor(self):
        # Checa linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return linha[0]
            
        # Checa colunas
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != ' ':
                return self.tabuleiro[0][coluna]

        # Checa diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return self.tabuleiro[0][0]

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return self.tabuleiro[0][2]
        
        return None  # Nenhum vencedor
    
    # UTILITY(state, player) -> number
    def calcular_utilidade(self, jogador):
        vencedor = self.verificar_vencedor()

        if vencedor == jogador:
            return 1  # Se for o jogador passado, retorna 1 (vitória)
        elif vencedor is not None:
            return -1  # Se houver vencedor (not None) e não for o jogador passado, retorna -1 (derrota)
        else:
            return 0  # Se for empate ou jogo em andamento, retorna 0
