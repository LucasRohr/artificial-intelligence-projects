from Tabuleiro import Tabuleiro
from JogadorHumano import JogadorHumano
from JogadorIA import JogadorIA

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador1 = None
        self.jogador2 = None

    def iniciar_jogo(self, is_humano_humano=False, is_humano_ia=False, is_ia_ia=False):
        # Reinicia o tabuleiro sempre que um novo jogo começar
        self.tabuleiro = Tabuleiro()

        # Limpa a tela
        print("\033c", end="")  # Comando ANSI para limpar a tela

        print("Bem-vindo ao Jogo da Velha!")

        if (is_humano_humano):
            print("Digite o nome do Jogador 1 (X): ")
            nome_jogador1 = input()
            self.jogador1 = JogadorHumano(nome_jogador1, "X")

            print("Digite o nome do Jogador 2 (O): ")
            nome_jogador2 = input()
            self.jogador2 = JogadorHumano(nome_jogador2, "O")

        if (is_humano_ia):
            print("Digite o nome do Jogador Humano (X): ")
            nome_jogador1 = input()
            self.jogador1 = JogadorHumano(nome_jogador1, "X")

            print("Jogador IA (O): IA Círculo")
            nome_jogador2 = "IA Círculo"
            self.jogador2 = JogadorIA(nome_jogador2, "O")

        if (is_ia_ia):
            print("Jogador IA 1 (X): IA Xis")
            nome_jogador1 = "IA Xis"
            self.jogador1 = JogadorIA(nome_jogador1, "X")

            print("Jogador IA 2 (O): IA Círculo")
            nome_jogador2 = "IA Círculo"
            self.jogador2 = JogadorIA(nome_jogador2, "O")

        print("Jogo da Velha Iniciado!")

        jogador_atual = self.jogador1  # Controla de quem é a vez de jogar

        # O jogo continua enquanto houver ações possíveis no tabuleiro
        while len(self.tabuleiro.gerar_acoes_possiveis()) > 0:
            # Exibe o estado atual do tabuleiro
            self.tabuleiro.exibir()

            # Jogador atual faz a jogada ou tenta novamente se a jogada for inválida
            if not jogador_atual.fazer_jogada(self.tabuleiro):
                continue

            # Caso houve um vencedor ou empate após a jogada do jogador atual, o jogo termina
            if self.tabuleiro.verificar_vencedor() is not None:
                # Exibe o estado final do tabuleiro
                self.tabuleiro.exibir()

                break

            # Alterna para o próximo jogador
            jogador_atual = self.jogador2 if jogador_atual == self.jogador1 else self.jogador1
