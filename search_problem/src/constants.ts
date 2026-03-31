// Custo de cada célula:
const COST = {
  movement: 1,
  traffic: 2,
  obstacle: Infinity,
  destination: 0,
} as const;

// Custo de cada célula do ambiente.
const CELL_COST: Record<string, number> = {
  free: COST.movement,
  traffic: COST.traffic,
  obstacle: COST.obstacle,
  destination: COST.destination,
};

// Direções possíveis para mover o agente.
const DIRECTIONS: [number, number][] = [
  [-1, 0], // up
  [1, 0], // down
  [0, -1], // left
  [0, 1], // right
];

export { COST, CELL_COST, DIRECTIONS };
