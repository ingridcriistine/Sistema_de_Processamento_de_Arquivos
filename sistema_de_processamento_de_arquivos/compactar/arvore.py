from .fila_prioridade import FilaDePrioridadeManual
from .node import Node

def construir_arvore_huffman(freq_map):
    pq = FilaDePrioridadeManual()

    for char, freq in freq_map.items():
        pq.add(Node(char=char, frequency=freq))

    while pq.size() > 1:
        n1 = pq.poll()
        n2 = pq.poll()

        novo = Node(
            char=None,
            frequency=n1.frequency + n2.frequency,
            left=n1,
            right=n2
        )

        pq.add(novo)

    return pq.poll()  # raiz da árvore
