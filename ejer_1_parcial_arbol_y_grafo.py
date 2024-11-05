from arbol_avl import BinaryTree

"""1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
caracteres–;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
"""""

pokemons = [
    {"nombre": "Bulbasaur","numero":1, "tipo": ["Planta", "Veneno"]},
    {"nombre": "Charmander","numero":4, "tipo": ["Fuego"]},
    {"nombre": "Squirtle","numero":7, "tipo": ["Agua"]},
    {"nombre": "Pikachu","numero":25, "tipo": ["Eléctrico"]},
    {"nombre": "Vulpix","numero":37, "tipo": ["Fuego"]},
    {"nombre": "Lycanroc","numero":745, "tipo": ["Roca"]},
    {"nombre": "Jolteon","numero":135, "tipo": ["Eléctrico"]},
    {"nombre": "Tyrantrum","numero":697, "tipo": ["Roca", "Dragón"]},
    {"nombre": "Meowth","numero":52, "tipo": ["Normal"]},
    {"nombre": "Gastly","numero":92, "tipo": ["Fantasma", "Veneno"]},
    {"nombre": "Eevee","numero":133, "tipo": ["Normal"]},
    {"nombre": "Mewtwo","numero":150, "tipo": ["Psíquico"]},
    {"nombre": "Chikorita","numero":152, "tipo": ["Planta"]},
    {"nombre": "Scizor","numero":212, "tipo": ["Bicho", "Acero"]},
    {"nombre": "Blaziken","numero":257, "tipo": ["Fuego", "Lucha"]},
    {"nombre": "Absol","numero":359, "tipo": ["Siniestro"]},
    {"nombre": "Garchomp","numero":445, "tipo": ["Dragón", "Tierra"]},
    {"nombre": "Lucario","numero":448, "tipo": ["Lucha", "Acero"]},
    {"nombre": "Rotom","numero":479, "tipo": ["Eléctrico", "Fantasma"]},
    {"nombre": "Excadrill","numero":530, "tipo": ["Tierra", "Acero"]},
    {"nombre": "Volcarona","numero":637, "tipo": ["Bicho", "Fuego"]},
    {"nombre": "Sylveon","numero":700, "tipo": ["Hada"]},
    {"nombre": "Regidrago","numero":895, "tipo": ["Dragón"]}
]

arbol_por_nombre = BinaryTree()
arbol_por_tipo = BinaryTree()
arbol_por_numero = BinaryTree()

for pokemon in pokemons:
    arbol_por_nombre.insert_node(pokemon['nombre'],pokemon['numero'],pokemon['tipo'])
    arbol_por_numero.insert_node(pokemon['numero'],pokemon['nombre'],pokemon['tipo'])
    arbol_por_tipo.insert_node(pokemon['tipo'],pokemon['nombre'],pokemon['numero'])



    
buscado = input("Inserte un nombre de pokemon para buscar para mostrar sus datos: ")
numero = int(input("Inserte un numero de la pokedex para mostrar sus datos: "))

#Para realizar esta busqueda, e impresión, tuve que agregar un atributo extra en la clase arbol_avl.py, llamado other_other_value
print("Los datos del pokemon buscado por numero son :", arbol_por_numero.search(1).value, arbol_por_numero.search(1).other_value, arbol_por_numero.search(1).other_other_value)
print()
print("Los datos del pokemon buscado por nombre son: ")
arbol_por_nombre.proximity_search(buscado)
print()
#Cree una función en la clase arbol_avl para poder analizar si el pokemon es del tipo especifico
print("La lista de nombres de los pokemons pertenecientes a los tipos agua, fuego, planta y eléctrico")
arbol_por_tipo.inorden_pokemons()
print()
print("El listado ordenado ascendentemente por numero es el siguiente: ")
arbol_por_numero.inorden()
print()
print("El listado ordenado ascendentemente por nombre es el siguiente: ")
arbol_por_nombre.inorden()
print()
print("El listado ordenado por nivel por nombre es el siguiente: ")
arbol_por_nombre.by_level()
print()
print("Los datos del pokemon Lycanroc:\n", arbol_por_nombre.search("Lycanroc").value, arbol_por_nombre.search("Lycanroc").other_value, arbol_por_nombre.search("Lycanroc").other_other_value)
print()
print("Los datos del pokemon Jolteon:\n", arbol_por_nombre.search("Jolteon").value, arbol_por_nombre.search("Jolteon").other_value, arbol_por_nombre.search("Jolteon").other_other_value)
print()
print("Los datos del pokemon Tyrantrum:\n", arbol_por_nombre.search("Tyrantrum").value, arbol_por_nombre.search("Tyrantrum").other_value, arbol_por_nombre.search("Tyrantrum").other_other_value)
print()
print("Hay un total de ", arbol_por_tipo.contar_pokemons("Eléctrico"), " pokemons eléctricos")
print("Hay un total de ", arbol_por_tipo.contar_pokemons("Acero"), " pokemons acero")