from grafo import Graph
"""14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.
"""

ambientes = ["cocina","comedor","cochera","quincho","baño 1","baño 2","habitacion 1","habitacion 2","terraza","patio","sala de estar"]

grafo = Graph(dirigido=False)

#a)

for ambiente in ambientes:
    nodo = {
        'value':ambiente,
        'aristas':[],
    }
    grafo.insert_vertice(ambiente)


#b)

grafo.insert_arista("cocina", "comedor", 1)
grafo.insert_arista("cocina", "cochera", 4)
grafo.insert_arista("cocina", "habitacion 1", 2)
grafo.insert_arista("comedor", "habitacion 1", 1)
grafo.insert_arista("comedor", "habitacion 2", 2)
grafo.insert_arista("comedor", "baño 1", 1)
grafo.insert_arista("cochera", "habitacion 2", 3)
grafo.insert_arista("cochera", "cocina", 3)
grafo.insert_arista("cochera", "quincho", 3)
grafo.insert_arista("quincho", "sala de estar", 5)
grafo.insert_arista("quincho", "habitacion 1", 4)
grafo.insert_arista("quincho", "patio", 2)
grafo.insert_arista("quincho", "terraza", 6)
grafo.insert_arista("quincho", "baño 2", 1)
grafo.insert_arista("baño 1", "habitacion 1", 2)
grafo.insert_arista("baño 1", "baño 2", 8)
grafo.insert_arista("baño 1", "cocina", 2)
grafo.insert_arista("baño 2", "habitacion 2", 6)
grafo.insert_arista("baño 2", "terraza", 7)
grafo.insert_arista("baño 2", "cocina", 7)
grafo.insert_arista("habitacion 1", "habitacion 2", 1)
grafo.insert_arista("habitacion 1", "cocina", 2)
grafo.insert_arista("habitacion 1", "terraza", 2)
grafo.insert_arista("habitacion 1", "sala de estar", 1)
grafo.insert_arista("habitacion 1", "patio", 3)
grafo.insert_arista("habitacion 2", "habitacion 1", 1)
grafo.insert_arista("habitacion 2", "cocina", 3)
grafo.insert_arista("habitacion 2", "baño 1", 2)
grafo.insert_arista("terraza", "comedor", 3)
grafo.insert_arista("terraza", "patio", 4)
grafo.insert_arista("terraza", "cochera", 4)
grafo.insert_arista("sala de estar", "cochera", 1)
grafo.insert_arista("sala de estar", "quincho", 2)
grafo.insert_arista("sala de estar", "patio", 1)
grafo.insert_arista("patio", "baño 1", 3)
grafo.insert_arista("patio", "cochera", 2)
grafo.insert_arista("patio", "terraza", 4)


#grafo.show_graph()

#c)

arbol_expansion_minima = grafo.kruskal("cocina")
print("Arbol de expansión minima:")
print()
total_metros = 0
for arista in arbol_expansion_minima[0].split(';'):
    origen, destino, peso = arista.split('-')
    total_metros+=int(peso)
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")
print()
print("Se necesitarian ", total_metros, " para conectar todos los ambientes")

#d)

camino_mas_corto = grafo.dijkstra("habitacion 1")

total_distancia = 0
camino = []

while camino_mas_corto.size() > 0:
    auxx= camino_mas_corto.on_top()
    if auxx[0]['value']!="sala de estar":
        aux = camino_mas_corto.pop()
        total_distancia+=aux[camino_mas_corto.size()-1]['peso']
    else:
        total_distancia+=aux[camino_mas_corto.size()-1]['peso']

print("El camino más corto de habitación 1 hasta sala de estar es el siguiente: ")
print(camino_mas_corto)
print("Se necesitan ", total_distancia, " metros de cable para conectar el router al Smart TV")