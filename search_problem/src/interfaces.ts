interface State {
  position: [number, number];
}

interface Node {
  state: State;
  parent: Node | null;
  cost: number;
}

interface Graph {
  nodes: Node[];
}

export type { State, Node, Graph };
