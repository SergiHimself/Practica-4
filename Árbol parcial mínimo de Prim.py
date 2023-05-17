# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:17:00 2023

@author: sergi
"""

import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

def prim(graph):
    # Inicializar el árbol parcial y el conjunto de nodos visitados
    minimum_spanning_tree = nx.Graph()
    visited = set()
    
    # Obtener un nodo inicial arbitrario
    start_node = list(graph.keys())[0]
    
    # Utilizar una cola de prioridad (heap) para seleccionar las aristas de menor peso
    heap = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    visited.add(start_node)
    
    while heap:
        # Obtener la arista de menor peso
        weight, node1, node2 = heappop(heap)
        
        # Si el otro nodo no ha sido visitado, agregar la arista al árbol parcial
        if node2 not in visited:
            visited.add(node2)
            minimum_spanning_tree.add_edge(node1, node2, weight=weight)
            
            # Agregar las aristas del nodo recién visitado a la cola de prioridad
            for neighbor, weight in graph[node2].items():
                if neighbor not in visited:
                    heappush(heap, (weight, node2, neighbor))
    
    return minimum_spanning_tree

# Ejemplo de grafo
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 1},
    'C': {'A': 2, 'E': 3},
    'D': {'B': 5, 'E': 2},
    'E': {'B': 1, 'C': 3, 'D': 2}
}

minimum_spanning_tree = prim(graph)

# Graficar el árbol parcial mínimo
pos = nx.spring_layout(minimum_spanning_tree)

# Dibujar el árbol parcial mínimo
nx.draw_networkx(minimum_spanning_tree, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
edge_labels = nx.get_edge_attributes(minimum_spanning_tree, 'weight')
nx.draw_networkx_edge_labels(minimum_spanning_tree, pos, edge_labels=edge_labels)

# Mostrar el árbol parcial mínimo
plt.axis('off')
plt.show()
