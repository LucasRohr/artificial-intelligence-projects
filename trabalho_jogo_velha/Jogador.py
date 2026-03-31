from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

    @abstractmethod
    def fazer_jogada(self, tabuleiro, posicao):
        pass
