from grafo import Graph

"""2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
algoritmos necesarios para resolver las siguientes tareas:
a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
cantidad de episodios en los que aparecieron juntos ambos personajes que se
relacionan;
b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
c) determinar cuál es el número máximo de episodio que comparten dos personajes,
d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8
"""
def episodios_maximos_compartidos(grafo):
    max_peso = 0
    for nodo in grafo.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
    return max_peso

def aristas_maximas_compartidas(grafo):
    max_peso = 0
    
    for nodo in grafo.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
                nodos = (nodo['value'], arista['value'])
    
    return max_peso, nodos

def arbol_expansion_minimo_yoda(graph):
    bosque = graph.kruskal("Yoda")
    contiene_yoda = any("Yoda" in arbol for arbol in bosque)
    return bosque, contiene_yoda

personajes_star_wars = [
    "Luke Skywalker",
    "Darth Vader",
    "Leia Organa",
    "Han Solo",
    "Obi-Wan Kenobi",
    "Yoda",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "Boba Fett",
    "Anakin Skywalker (joven)",
    "Padmé Amidala",
    "Mace Windu",
    "Qui-Gon Jinn",
    "Ahsoka Tano",
    "Darth Maul",
    "Kylo Ren (Ben Solo)",
    "Rey",
    "Finn",
    "Poe Dameron",
    "Jango Fett",
    "Lando Calrissian",
    "General Leia Organa",
    "Supreme Leader Snoke",
    "Jar Jar Binks",
    "Count Dooku (Darth Tyranus)",
    "Grievous",
    "Jyn Erso",
    "Cassian Andor",
    "K-2SO",
    "Boba Fett",
    "BB-8"
]

grafo = Graph(dirigido=False)

for personaje in personajes_star_wars:
    nodo = {
        'value': personaje,
        'aristas':[],
    }
    grafo.insert_vertice(personaje)

grafo.insert_arista("Luke Skywalker", "Leia Organa", 3)
grafo.insert_arista("Luke Skywalker", "Rey", 1)
grafo.insert_arista("Luke Skywalker", "Darth Vader", 3)
grafo.insert_arista("Han Solo", "Leia Organa", 2)
grafo.insert_arista("Han Solo", "Chewbacca", 6)
grafo.insert_arista("Obi-Wan Kenobi", "Anakin Skywalker", 3)
grafo.insert_arista("Obi-Wan Kenobi", "Darth Vader", 2)
grafo.insert_arista("Yoda", "Obi-Wan Kenobi", 4)
grafo.insert_arista("Anakin Skywalker", "Padmé Amidala", 2)
grafo.insert_arista("Ashoka Tano", "Anakin Skywalker", 2)
grafo.insert_arista("Kylo Ren(Ben Solo)", "Leia Organa", 3)
grafo.insert_arista("Kylo Ren(Ben Solo)", "Han Solo", 1)
grafo.insert_arista("Darth Maul", "Qui-Gon Jinn", 1)
grafo.insert_arista("Darth Maul", "Obi-Wan Kenobi", 2)
grafo.insert_arista("Jyn Erso", "Cassian Andor", 1)
grafo.insert_arista("Jyn Erso", "K-2SO", 1)
grafo.insert_arista("Rey", "Kylo Ren (Ben Solo)", 3)
grafo.insert_arista("Lando Clarissian", "Han Solo", 3)

bosque, yoda_presente = arbol_expansion_minimo_yoda(grafo)
print("Árbol de expansión mínimo contiene a Yoda:", yoda_presente)
print("")
peso_maximo, nodos_conectados = aristas_maximas_compartidas(grafo)
print("La arista más grande tiene un peso de {peso_maximo} y conecta a los nodos: {nodos_conectados[0]} y {nodos_conectados[1]}")
print()
max_peso = episodios_maximos_compartidos(grafo)
print(f"El número máximo de episodios que comparten dos personajes es: {max_peso}")

#grafo.show_graph()