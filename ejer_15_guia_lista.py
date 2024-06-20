from random import randint
from lista import search, by_name, show_list, show_list_list, by_torneos_ganados, by_nivel
"""Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;

j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;

k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;"""

entrenadores = [
{
"nombre": "Ash Ketchum",
"torneos_ganados": 7,
"batallas_perdidas": 50,
"batallas_ganadas": 120
},
{
"nombre": "Goh",
"torneos_ganados": 2,
"batallas_perdidas": 10,
"batallas_ganadas": 40
},
{
"nombre": "Leon",
"torneos_ganados": 10,
"batallas_perdidas": 5,
"batallas_ganadas": 100
},
{
"nombre": "Chloe",
"torneos_ganados": 1,
"batallas_perdidas": 8,
"batallas_ganadas": 30
},
{
"nombre": "Raihan",
"torneos_ganados": 4,
"batallas_perdidas": 15,
"batallas_ganadas": 60
}
]

pokemons =[
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({"sublist":[]})
    lista_entrenadores.append(entrenador)
    
lista_entrenadores.sort(key=by_name)

for pokemon in pokemons:
    posicion = search(lista_entrenadores,"nombre", entrenadores[randint(0,4)]["nombre"])
    if posicion is not None:
        lista_entrenadores[posicion]["sublist"].append(pokemon)
    else:
        print("El entrenador no está en la lista")

def cantidad_pokemons(lista, buscado):
    return len(lista[search(lista,"nombre", buscado)]["sublist"])

def mas_de_tres_torneos(lista):
    lista_ganadores=[]
    for entrenador in lista_entrenadores:
        if entrenador["torneos_ganados"] > 3:
            lista_ganadores.append(entrenador["nombre"])
    return lista_ganadores

def mas_victorias_y_nivel(lista):
    lista_entrenadores.sort(key=by_torneos_ganados)
    lista_entrenadores[0]["sublist"].sort(key=by_nivel)
    pokemonFuerte = lista_entrenadores[0]["sublist"][0]
    print(lista_entrenadores[0]["nombre"],"es el entrenador con más torneos ganados y su pokemon con mayor nivel es", pokemonFuerte["nombre"])

def datos_entrenador_y_pokemon(lista, buscado):
    print("Datos del entrenador buscado:",lista[search(lista,"nombre", buscado)])
    print()
    print("Datos de sus pokemons:",lista[search(lista,"nombre", buscado)]["sublist"])

def porcentaje_mas_79(lista):
    lista_entrenadores = []
    for entrenador in lista:
        if(entrenador["batallas_ganadas"]/(entrenador["batallas_ganadas"]+entrenador["batallas_perdidas"]))*100 > 79:
            lista_entrenadores.append(entrenador["nombre"])
    return lista_entrenadores

def fuego_y_planta_agua_volador(lista):
    lista_entrenadores = []
    for entrenador in lista:
        if lista_entrenadores.count(entrenador["nombre"] == 0):
            for pokemon in entrenador["sublist"]:
                if (pokemon["tipo"] is not None) and (pokemon["subtipo"] is not None):
                    if "planta" or "fuego" in pokemon["tipo"]:
                        lista_entrenadores.append(entrenador["nombre"])
                    elif "planta" or "fuego" in pokemon["subtipo"]:
                        lista_entrenadores.append(entrenador["nombre"])
                    elif (pokemon["tipo"] == "agua") and (pokemon["subtipo"] == "volador"):
                        lista_entrenadores.append(entrenador["nombre"])
    return lista_entrenadores

def promedio_nivel(lista,buscado):
    promedio = 0
    for pokemon in lista[search(lista,"nombre", buscado)]["sublist"]:
        promedio += pokemon["nivel"]
    return promedio/len(lista[search(lista,"nombre", buscado)]["sublist"])

def pokemonx_por_entrenador(lista, buscado):
    lista_entrenadores=[]
    for entrenador in lista:
        for pokemon in entrenador["sublist"]:
            if pokemon["nombre"] == buscado  and (lista_entrenadores.count(entrenador["nombre"]) == 0):
                lista_entrenadores.append(entrenador["nombre"])
    return lista_entrenadores


buscado= input("Por favor ingrese el entrenador del que desea saber cuantos pokemons tiene: ")
pokemon_buscado= input("Por favor ingrese pokemon que desee buscar: ")
print()
print("La cantidad de pokemons de", buscado," es de:", cantidad_pokemons(lista_entrenadores, buscado))
print()
print("Los siguientes entrenadores han ganado más de tres torneos:", mas_de_tres_torneos(lista_entrenadores))
print()
mas_victorias_y_nivel(lista_entrenadores)
print()
datos_entrenador_y_pokemon(lista_entrenadores, buscado)
print()
print(porcentaje_mas_79(lista_entrenadores))
print()
print(fuego_y_planta_agua_volador(lista_entrenadores))
print()
print(promedio_nivel(lista_entrenadores, buscado))
print()
print(pokemonx_por_entrenador(lista_entrenadores, pokemon_buscado))