from Jogo import Jogo

def main():
    # Inicializa classe do jogo
    jogo = Jogo()

    # =========================================
    # == Jogo com ambos os jogadores humanos ==
    # =========================================

    jogo.iniciar_jogo(is_humano_humano=True)

    # Verifica o resultado do jogo e exibe o vencedor ou empate
    utilidade_jogador_1 = jogo.tabuleiro.calcular_utilidade(jogo.jogador1.simbolo)
    utilidade_jogador_2 = jogo.tabuleiro.calcular_utilidade(jogo.jogador2.simbolo)

    if utilidade_jogador_1 == 1:
        print(f"\n{jogo.jogador1.nome} venceu!")
    elif utilidade_jogador_2 == 1:
        print(f"\n{jogo.jogador2.nome} venceu!")
    else:
        jogo.tabuleiro.exibir()  # Exibe o estado final do tabuleiro
        print("\nO jogo terminou empatado!")

    # =========================================
    # == Jogo com jogador humano vs IA ==
    # =========================================

    jogo.iniciar_jogo(is_humano_ia=True)

    # Verifica o resultado do jogo e exibe o vencedor ou empate
    utilidade_jogador_1 = jogo.tabuleiro.calcular_utilidade(jogo.jogador1.simbolo)
    utilidade_jogador_2 = jogo.tabuleiro.calcular_utilidade(jogo.jogador2.simbolo)

    if utilidade_jogador_1 == 1:
        print(f"\n{jogo.jogador1.nome} venceu!")
    elif utilidade_jogador_2 == 1:
        print(f"\n{jogo.jogador2.nome} venceu!")
    else:
        jogo.tabuleiro.exibir()  # Exibe o estado final do tabuleiro
        print("\nO jogo terminou empatado!")

    # =========================================
    # == Jogo com ambas as IAs ==
    # =========================================

    jogo.iniciar_jogo(is_ia_ia=True)

    # Verifica o resultado do jogo e exibe o vencedor ou empate
    utilidade_jogador_1 = jogo.tabuleiro.calcular_utilidade(jogo.jogador1.simbolo)
    utilidade_jogador_2 = jogo.tabuleiro.calcular_utilidade(jogo.jogador2.simbolo)

    if utilidade_jogador_1 == 1:
        print(f"\n{jogo.jogador1.nome} venceu!")
    elif utilidade_jogador_2 == 1:
        print(f"\n{jogo.jogador2.nome} venceu!")
    else:
        jogo.tabuleiro.exibir()  # Exibe o estado final do tabuleiro
        print("\nO jogo terminou empatado!")

# Executa o jogo quando o script for executado diretamente
if __name__ == "__main__":
    main()