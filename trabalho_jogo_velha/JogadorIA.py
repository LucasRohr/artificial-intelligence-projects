from Jogador import Jogador

class JogadorIA(Jogador):
    def __init__(self, nome, simbolo):
        super().__init__(nome, simbolo)

    def fazer_jogada(self, tabuleiro):
        profundidade = 0
        melhor_pontuacao = float('-inf')
        melhor_jogada = None

        for acao in tabuleiro.gerar_acoes_possiveis():
            # Primeiro, faz a jogada (avança na árvore de decisões)
            tabuleiro.fazer_jogada(acao, self.simbolo)

            # Depois, chama o Minimax para avaliar o resultado desse caminho de jogada
            pontuacao = self.minimax(tabuleiro, profundidade + 1, False)

            # Compara a pontuação obtida com a melhor pontuação encontrada até agora pelo minimax
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao # Atualiza a melhor pontuação
                melhor_jogada = acao # Atualiza a melhor jogada

            # Reverte a jogada para explorar outras possibilidades (volta na árvore de decisões)
            tabuleiro.desfazer_jogada(acao)

        # Faz a melhor jogada encontrada pela exploração do Minimax na árvore de decisões
        if melhor_jogada is not None:
            tabuleiro.fazer_jogada(melhor_jogada, self.simbolo)
            print(f"{self.nome} ({self.simbolo}) fez uma jogada na posição ({melhor_jogada[0] + 1}, {melhor_jogada[1] + 1}).")
            return True
        
        return False

    def minimax(self, tabuleiro, profundidade, is_maximizando):
        acoes_possiveis = tabuleiro.gerar_acoes_possiveis()

        # Jogo acabou se não houver mais ações possíveis ou se houver um vencedor
        is_jogo_acabou = len(acoes_possiveis) == 0 or tabuleiro.verificar_vencedor() is not None

        if is_jogo_acabou:
            # Se acabou, primeiro calcula a utilidade final com base no resultado do jogo para a IA
            pontuacao_base = tabuleiro.calcular_utilidade(self.simbolo)

            # Se for vitória da IA (+1), subtrai a profundidade para valorizar vitórias rápidas
            if pontuacao_base == 1:
                return pontuacao_base - (profundidade * 0.1)
            # Se for derrota da IA (-1), soma a profundidade para preferir resistir mais tempo
            elif pontuacao_base == -1:
                return pontuacao_base + (profundidade * 0.1)
            # Empate retorna 0
            else:
                return 0
        
        if is_maximizando:
            melhor_pontuacao = float('-inf')

            for acao in acoes_possiveis:
                # Primeiro, faz a jogada (avança na árvore de decisões)
                tabuleiro.fazer_jogada(acao, self.simbolo)

                # Depois, chama o Minimax para avaliar o resultado desse caminho de jogada
                pontuacao = self.minimax(tabuleiro, profundidade + 1, False)

                # Reverte a jogada para explorar outras possibilidades (volta na árvore de decisões)
                tabuleiro.desfazer_jogada(acao)
                
                # Compara a pontuação obtida com a melhor pontuação encontrada até agora
                melhor_pontuacao = max(pontuacao, melhor_pontuacao)

            return melhor_pontuacao
        
        else:
            melhor_pontuacao = float('inf')

            for acao in acoes_possiveis:
                # Primeiro, faz a jogada (avança na árvore de decisões)
                # Simula a jogada do oponente, tentando minimizar a pontuação para a IA
                tabuleiro.fazer_jogada(acao, 'O' if self.simbolo == 'X' else 'X')

                # Depois, chama o Minimax para avaliar o resultado desse caminho de jogada
                pontuacao = self.minimax(tabuleiro, profundidade + 1, True)

                # Reverte a jogada para explorar outras possibilidades (volta na árvore de decisões)
                tabuleiro.desfazer_jogada(acao)
                
                # Compara a pontuação obtida com a melhor pontuação encontrada até agora
                # Minimiza a pontuação para a IA, assumindo que o oponente joga da melhor forma possível
                melhor_pontuacao = min(pontuacao, melhor_pontuacao)

            return melhor_pontuacao