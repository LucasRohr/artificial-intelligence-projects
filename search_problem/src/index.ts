import { environmentMap } from "./environment_map";
import { CELL_COST, COST, DIRECTIONS } from "./constants";
import { Queue } from "./queue";

import type { Node, Graph } from "./interfaces";

// Nome: Lucas Rohr Carreño

// Problema escolhido:
// Ir de uma posição inicial para uma posição final em um ambiente que representa um mapa de uma cidade.
// O ambiente é representado por uma matriz de células, onde cada célula pode ser um obstáculo, um caminho livre ou um caminho com tráfego.
// Ao longo do caminho, o agente deve evitar obstáculos e minimizar o custo de viagem.
// Alguns caminhos podem ter mais ou menos tráfego, o que pode afetar o custo de viagem.
// O agente deve encontrar o caminho com menor tamanho e/ou custo para chegar ao destino.

// Estado inicial:
// - Posição: (0, 0) - A posição inicial do agente.

// Estado final:
// - Posição: (8, 8) - A posição final do agente que escolhi como destino.

// Ações:
// - Mover para uma das células vizinhas (direita, esquerda, cima, baixo)
// - Célula vizinha pode ser livre, com tráfego ou ser o destino
// - Não é possível mover para uma célula que é um obstáculo.

// Função de custo:
// - Custo de movimento: 1 - Custo de movimentar o agente para uma célula vizinha.
// - Custo de tráfego: 2 - Custo de movimentar o agente para uma célula com tráfego.
// - Custo de destino: 0 - Custo de chegar ao destino.

// Algoritmo de busca escolhido: BFS
// Utilizado para gerar o caminho com menor número de hops entre nós e potencialmente menor custo de viagem.

// Prints da execução:
// Acesse a pasta "execution_prints" para ver os prints da execução.

// Converte o ambiente em um grafo para aplicar a busca em largura
function mapEnvironmentToGraph(map: string[][]): Graph {
  const graph: Graph = { nodes: [] };

  // Itera sobre cada célula do ambiente
  for (let row = 0; row < map.length; row++) {
    for (let col = 0; col < (map[row]?.length ?? 0); col++) {
      const cell = map[row]?.[col];

      // Se a célula for undefined ou for um obstáculo, continua para a próxima célula
      if (!cell || cell === "obstacle") continue;

      // Cria um novo nó para a célula
      const node: Node = {
        state: { position: [row, col] },
        parent: null,
        cost: CELL_COST[cell] ?? COST.movement,
      };

      // Adiciona o novo nó ao grafo
      graph.nodes.push(node);
    }
  }

  return graph; // Retorna o grafo representando o ambiente
}

// Obtém os vizinhos de um nó do grafo que representa o ambiente
function getNeighbors(node: Node, map: string[][], graph: Graph): Node[] {
  const [row, col] = node.state.position;
  const neighbors: Node[] = [];

  for (const [directionRow, directionCol] of DIRECTIONS) {
    // Calcula a nova posição do vizinho
    const newRow = row + directionRow;
    const newCol = col + directionCol;
    const cell = map[newRow]?.[newCol];

    // Se a célula for undefined ou for um obstáculo, continua para o próximo vizinho
    if (!cell || cell === "obstacle") continue;

    // Obtém o vizinho do nó se ele existir
    const neighbor: Node | undefined = graph.nodes.find(
      (node) =>
        node.state.position[0] === newRow && node.state.position[1] === newCol
    );

    // Se o vizinho existir, adiciona no array de vizinhos
    if (neighbor) {
      neighbors.push(neighbor);
    }
  }

  // Retorna os vizinhos do nó
  return neighbors;
}

// Gera uma chave única para o nó com base na sua posição
function getNodePositionKey(node: Node): string {
  return node.state.position.join(",");
}

// Realiza a busca em largura para encontrar o caminho com menor custo desde o nó inicial até o nó final
function bfsSearch(
  graph: Graph,
  map: string[][],
  initialPos: [number, number],
  finalPos: [number, number]
): void {
  // Obtém o nó inicial do grafo
  const startNode: Node | undefined = graph.nodes.find(
    (n) =>
      n.state.position[0] === initialPos[0] &&
      n.state.position[1] === initialPos[1]
  );

  if (!startNode) {
    console.log("Não foi possível encontrar o nó inicial no grafo.");
    return;
  }

  // Tipo para armazenar o nó atual, o caminho percorrido e o custo acumulado na fila
  type QueueEntry = {
    node: Node;
    pathData: { idPath: number; path: Node[] };
    accumulatedCost: number;
  };

  const frontier = new Queue<QueueEntry>(); // Fila/fronteira para armazenar os nós a serem visitados
  const visited = new Set<string>(); // Set para armazenar os nós já visitados
  const visitedNodes: Node[] = []; // Array para armazenar os nós já visitados

  // Adiciona o nó inicial à fila/fronteira
  let idPath: number = 1;

  frontier.enqueue({
    node: startNode,
    pathData: { idPath: idPath++, path: [startNode] },
    accumulatedCost: startNode.cost,
  });

  // Enquanto a fila/fronteira não estiver vazia, processa os nós a serem visitados
  while (!frontier.isEmpty()) {
    const frontierEntry = frontier.dequeue()!; // Remove o primeiro nó da fila/fronteira
    const { node, pathData, accumulatedCost } = frontierEntry;
    const key = getNodePositionKey(node);

    // Se o nó já foi visitado, continua para o próximo nó
    if (visited.has(key)) continue;

    visited.add(key); // Adiciona o nó visitado ao set
    visitedNodes.push(node); // Adiciona o nó visitado ao array

    const [row, col] = node.state.position;

    console.log(
      `[Caminho ${pathData.idPath}]  Nó visitado: (${row}, ${col})  Célula: ${map[row]?.[col]}  Custo: ${node.cost}  Custo acumulado: ${accumulatedCost}`
    );

    // Se o nó atual for o nó final, imprime o caminho percorrido e o custo acumulado
    const isFinalNode = row === finalPos[0] && col === finalPos[1];

    if (isFinalNode) {
      console.log("\n=== Destino alcançado! ===");
      console.log(`Total de nós visitados: ${visitedNodes.length}`);
      console.log(`Custo total do caminho: ${accumulatedCost}`);
      console.log(
        `Melhor caminho: ${pathData.idPath} → ${pathData.path.length} nós`
      );

      // Itera sobre o caminho percorrido até o nó final
      for (const step of pathData.path) {
        const [row, col] = step.state.position;

        console.log(
          `Posição: (${row}, ${col})  Célula: ${map[row]?.[col]}  Custo: ${step.cost}`
        );
      }
      return; // Para quando chegar no nó final, que é o destino
    }

    // Itera sobre os vizinhos do nó atual
    const neighbors = getNeighbors(node, map, graph);

    let isFirstNeighbor = true;

    for (const neighbor of neighbors) {
      // Se o vizinho não foi visitado, adiciona na fila/fronteira
      const neighborKey = getNodePositionKey(neighbor);

      if (!visited.has(neighborKey)) {
        // Adiciona o nó pai para a reconstrução do caminho
        const neighborWithParent: Node = { ...neighbor, parent: node };

        // O primeiro vizinho continua no mesmo caminho (herda o idPath do pai).
        // A partir do segundo vizinho o caminho bifurca, então recebe um novo id.
        const neighborIdPath = isFirstNeighbor ? pathData.idPath : idPath++;
        isFirstNeighbor = false;

        // Adiciona o vizinho à fila/fronteira
        frontier.enqueue({
          node: neighborWithParent,
          pathData: {
            idPath: neighborIdPath,
            path: [...pathData.path, neighborWithParent],
          },
          accumulatedCost: accumulatedCost + neighbor.cost,
        });
      }
    }
  }

  console.log("\nNão foi possível encontrar um caminho para o destino.");
}

function main(): void {
  const initialPos: [number, number] = [0, 0]; // Posição inicial do agente
  const finalPos: [number, number] = [8, 8]; // Posição final do agente

  // Converte o ambiente em um grafo para aplicar a busca em largura
  const graph = mapEnvironmentToGraph(environmentMap);

  console.log("=== BFS Search ===");
  console.log(`Início: (${initialPos})  →  Destino: (${finalPos})\n`);

  bfsSearch(graph, environmentMap, initialPos, finalPos);
}

main();
