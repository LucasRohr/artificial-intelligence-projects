// Fila para armazenar os nós a serem visitados no grafo que representa o ambiente
export class Queue<T> {
  private items: T[] = [];

  // Adiciona um item à fila
  enqueue(item: T): void {
    this.items.push(item);
  }

  // Remove e retorna o primeiro item da fila
  dequeue(): T | undefined {
    return this.items.shift();
  }

  // Verifica se a fila está vazia
  isEmpty(): boolean {
    return this.items.length === 0;
  }

  // Retorna o tamanho da fila
  size(): number {
    return this.items.length;
  }
}
