##Una empresa requiere transportar X cantidad de peso por una ruta por definir entre dospuntos de acuerdo al grafo de la parte inferior, calcular el costo de transportar la cargaentre dos puntos si el km de recorrido es a $2.000 por cada 150 kg y los tramos entrecada NODO son en Km. Se debe generar una factura para el cliente, especificando el origen y destino, la ruta a seguir y el costo del transporte. 

import matplotlib.pyplot as plt
import os
import networkx as nx
from itertools import permutations

# Función para encontrar el árbol recorredor mínimo en forma de ruta
def find_minimum_spanning_tree(graph):
    mst = nx.minimum_spanning_tree(graph)
    return list(nx.dfs_edges(mst, source="A"))

# Función para encontrar el camino hamiltoniano sin repetir nodos
def find_hamiltonian_path(graph):
    # Generar todas las permutaciones de nodos
    all_permutations = permutations(graph.nodes)
    
    # Verificar cada permutación para encontrar un camino hamiltoniano
    for perm in all_permutations:
        if all(graph.has_edge(perm[i], perm[i + 1]) for i in range(len(perm) - 1)):
            return list(perm)
    
    return None

# Crear un grafo ponderado
G = nx.Graph()

# Añadir nodos
nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

# Añadir aristas con pesos
edges_with_weights = [
    ("A", "B", 3),
    ("B", "C", 4.3),
    ("B", "D", 6.5),
    ("C", "E", 3.5),
    ("D", "E", 4.5),

]
G.add_weighted_edges_from(edges_with_weights)

# Especificar posiciones personalizadas para cada nodo
custom_positions = {"A": (0, 0), "B": (0.4, 0.7), "C": (0.5, 0.1), "D": (1.8, 0.8), "E": (1.3, 0.06), "F": (0.9, 0), "G": (1.8, -0.2)}

while True:
    # Dibujar el grafo con posiciones personalizadas
    nx.draw(G, pos=custom_positions, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos=custom_positions, edge_labels=nx.get_edge_attributes(G, 'weight'))
    
    # Mostrar el grafo
    plt.show()
    
    

    
    # Leer la opción del usuario
    inicio = input("Digite el nodo de inicio: ")
    final = input("Digite el nodo final: ")
    
    ##validar que los nodos existan
    while inicio not in nodes or final not in nodes:
        print("Los nodos ingresados no existen")
        inicio = input("Digite el nodo de inicio: ")
        final = input("Digite el nodo final: ")
    
    #pedir la carga a transportar
    carga = int(input("Digite la carga a transportar: "))
    
    
    ##validar que los nodos sean diferentes
    while inicio == final:
        print("Los nodos ingresados son iguales")
        inicio = input("Digite el nodo de inicio: ")
        final = input("Digite el nodo final: ")
        
    ##encontrar el camino más corto
    shortest_path = nx.shortest_path(G, inicio, final, weight="weight")
    print("\nEl camino más corto es: ", shortest_path)
    
    ##encontrar el costo del camino más corto
    costo = nx.shortest_path_length(G, inicio, final, weight="weight")
    print("El costo del camino más corto es: ", (round(costo*(carga/150)*2000)))
    
    ##gENERAR LA FACTURA en un archivo de texto
    factura = open("factura.txt", "w")
    factura.write("Factura de transporte\n")
    factura.write("Origen: "+inicio+"\n")
    factura.write("Destino: "+final+"\n")
    factura.write("Ruta: "+str(shortest_path)+"\n")
    factura.write("Costo del transporte: "+str(round(costo*(carga/150)*2000))+"\n")
    factura.close()
    
    ##abrir bloc de notas con la factura
    os.system("notepad.exe factura.txt")
    
    