from Jogador import Jogador

class JogadorHumano(Jogador):
    def fazer_jogada(self, tabuleiro):
        print(f"{self.nome} ({self.simbolo}), é sua vez de jogar.")
        print("Digite a posição da jogada (linha e coluna, separadas por espaço): ")

        input_usuario = input().split()
        linha, coluna = map(int, input_usuario)

        resultado_jogada = tabuleiro.fazer_jogada((linha, coluna), self.simbolo)

        if resultado_jogada:
            print(f"{self.nome} fez uma jogada na posição ({linha}, {coluna}).")
            return True
        else:
            print("Posição já ocupada ou inválida. Tente novamente.")
            return False
