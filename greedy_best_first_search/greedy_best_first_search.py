# Nome: Lucas Rohr Carreño

import random
import heapq # Para implementar a fila de prioridade usada na busca
from colorama import init, Fore

init(autoreset=True)

class GreedyBestFirstSearch:
    move_options = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Direções: direita, baixo, esquerda, cima

    def __init__(self, maze, start_A, goal_B):
        self.maze = maze # Labiritinto passado como parametro ou gerado aleatoriamente
        self.start_A = start_A # Ponto de partida
        self.goal_B = goal_B # Ponto de chegada
        self.visited = set() # Set de nós visitados
        self.path = [] # Caminho encontrado
        self.nodes_explored = 0 # Número de nós explorados
    
    def heuristic(self, node):
        # Usando distancia de Manhattan como heuristica
        return abs(node[0] - self.goal_B[0]) + abs(node[1] - self.goal_B[1])

    def generate_maze(self):
        if (self.maze):
            self.maze = self.maze
        else:
            # Gera labirinto aleatório onde 0 representa parede
            # e celulas livres contém o valor 1
            maze = []

            # Labirinto 12x12
            for i in range(12):
                row = []
                for j in range(12):
                    # 30% de change de parede, 70% de chance de célula livre
                    if random.random() < 0.3:
                        row.append(0)  # Parede
                    else:
                        row.append(1) # Célula livre
                maze.append(row)

            # Garante que o início e o fim estejam livres
            maze[self.start_A[0]][self.start_A[1]] = 1
            maze[self.goal_B[0]][self.goal_B[1]] = 1
            self.maze = maze
        
    def is_valid_move(self, node):
        x, y = node

        # Verifica os limites da matriz
        is_outside_limits = x < 0 or x >= len(self.maze) or y < 0 or y >= len(self.maze[0])

        if is_outside_limits:
            return False
        
        # Verifica se é parede (0 representa obstáculo/bloqueio)
        if self.maze[x][y] == 0:
            return False
        
        return True
    
    def search(self):
        # Fronteira é a fila de prioridade
        frontier = []

        # Insere tuplas no formato: (valor_heuristica, node)
        # Insere primeiro nó na fronteira
        heapq.heappush(frontier, (self.heuristic(self.start_A), self.start_A))

        # Dicionário para tracking do caminho e reconstruir o path final
        came_from = {self.start_A: None}

        # Loop principal
        while frontier:
            # Remove o nó com a menor heurística da fronteira e atribui como current_node
            _, current_node = heapq.heappop(frontier)

            # Teste se chegou no objetivo
            if current_node == self.goal_B:
                self.visited.add(current_node) # Marca o nó objetivo como visitado
                self.nodes_explored += 1 # Incrementa o contador de nós explorados
                self.path = self._reconstruct_path(came_from, current_node) # Retorna caminho reconstruído
                return self.path
            
            # Se já visitou, pula para o próximo nó na fronteira
            if current_node in self.visited:
                continue

            self.visited.add(current_node) # Marca o nó atual como visitado
            self.nodes_explored += 1 # Incrementa o contador de nós explorados

            # Expende os nós vizinhos para cada opção de movimento (direção)
            for move in self.move_options:
                neighbor = (current_node[0] + move[0], current_node[1] + move[1])

                # Se for válido e não explorado, adiciona na fronteira
                if self.is_valid_move(neighbor) and neighbor not in self.visited:
                    if neighbor not in came_from: # Evita adicionar o mesmo nó várias vezes na fronteira
                        came_from[neighbor] = current_node # Adiciona o nó atual como anterior ao vizinho
                        # Adiciona o vizinho na fronteira com sua heurística como prioridade
                        heapq.heappush(frontier, (self.heuristic(neighbor), neighbor))

        # Se a fronteira esvaziar e não achar o objetivo, retorna None
        return None
    
    def _reconstruct_path(self, came_from, current):
        # Faz o caminho inverso do objetivo até o início
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]

        path.reverse() # Inverte o caminho para ter a ordem correta do início até o objetivo

        return path
    
    def print_maze_result(self):
        print("\n--- Visualização do Labirinto ---")

        for i, row in enumerate(self.maze):
            cells = []
            for j, cell in enumerate(row):
                if cell == 0:
                    cells.append(Fore.WHITE + "XX") # Parede
                else:
                    # Calcula a heurística para exibir e formata com 2 dígitos
                    heuristic_value = self.heuristic((i, j))
                    heuristic_formatted = f"{heuristic_value:02d}"

                    is_path_cell = (i, j) in self.path
                    is_visited = (i, j) in self.visited

                    if is_path_cell:
                        cells.append(Fore.GREEN + heuristic_formatted) # Célula no caminho em verde
                    elif is_visited:
                        cells.append(Fore.YELLOW + heuristic_formatted) # Célula visitada em amarelo
                    else:
                        cells.append(heuristic_formatted) # Célula livre não visitada em branco

            print(" ".join(cells))

    def print_results(self, search_result):
        print(f"\nNúmero de nós explorados: {self.nodes_explored}")

        if search_result is None:
            print("Caminho não encontrado.")
        else:
            print(f"Comprimento do caminho: {len(self.path)}")
            print("Caminho encontrado:", self.path)

# Execução do algoritmo
if __name__ == "__main__":
    # Exemplo com labirinto gerado aleatoriamente
    print("=== Teste com Labirinto Aleatório ===")

    greedyBestFirstSearch = GreedyBestFirstSearch(maze=None, start_A=(0, 0), goal_B=(11, 11))
    greedyBestFirstSearch.generate_maze() # Gera um labirinto aleatório
    search_result = greedyBestFirstSearch.search() # Executa a busca e armazena o resultado
    greedyBestFirstSearch.print_maze_result() # Imprime o labirinto com as células visitadas
    greedyBestFirstSearch.print_results(search_result) # Imprime o caminho encontrado

    # Exemplo com labirinto pré-definido
    print("\n=== Teste com Labirinto Pré-definido ===")

    predefined_maze = [
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
    ]

    greedyBestFirstSearch = GreedyBestFirstSearch(maze=predefined_maze, start_A=(0, 0), goal_B=(11, 11))
    search_result = greedyBestFirstSearch.search() # Executa a busca e armazena o resultado
    greedyBestFirstSearch.print_maze_result() # Imprime o labirinto com as células visitadas
    greedyBestFirstSearch.print_results(search_result) # Imprime o caminho encontrado
