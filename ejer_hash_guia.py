# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a 
# su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrico, Hielo

pokemons=[
    {"nombre": "Bulbasaur", "tipo": "Plantas/Veneno", "nivel": 5, "numero": 1},
    {"nombre": "Charmander", "tipo": "Fuego", "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": "Agua", "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": "Eléctrico", "nivel": 61, "numero": 25},
    {"nombre": "Jigglypuff", "tipo": "Normal/Hada", "nivel": 5, "numero": 39},
    {"nombre": "Meowth", "tipo": "Normal", "nivel": 1, "numero": 52},
    {"nombre": "Psyduck", "tipo": "Agua", "nivel": 25, "numero": 54},
    {"nombre": "Machop", "tipo": "Lucha", "nivel": 38, "numero": 66},
    {"nombre": "Tentacool", "tipo": "Agua/Veneno", "nivel": 55, "numero": 72},
    {"nombre": "Geodude", "tipo": "Roca/Tierra", "nivel": 10, "numero": 74},{
    "nombre": "Nidorino" , "tipo": "Veneno", "nivel": 32, "numero":33 },{
    "nombre": "Blastoise" , "tipo": "Agua", "nivel": 5, "numero":9},{
    "nombre": "Glaceon" , "tipo": "Hielo", "nivel": 5 , "numero":471},{
    "nombre": "Duraludon" , "tipo": "Acero", "nivel": 8 , "numero":884}
]

# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base a 
# su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
def hash_tipo_poke(pokemons):
    return pokemons["tipo"].split("/")[0]

def hash_ultimo_digito(pokemons):
    return pokemons["numero"]%10

def hash_nivel(pokemons):
     return pokemons["nivel"]%10
        
lista_tipo_poke={}
lista_ultimo_digito={}
lista_nivel={}


# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
for pokemon in pokemons:
    value=hash_tipo_poke(pokemon)
    if value not in lista_tipo_poke:
        lista_tipo_poke[value]=[]
    lista_tipo_poke[value].append(pokemon)
         
    value2=hash_ultimo_digito(pokemon)
    if value2 not in lista_ultimo_digito:
        lista_ultimo_digito[value2]=[]
    lista_ultimo_digito[value2].append(pokemon)

    value3=hash_nivel(pokemon)
    if value3 not in lista_nivel:
        lista_nivel[value3]=[]
    lista_nivel[value3].append(pokemon)

print (lista_tipo_poke)
print()
print(lista_ultimo_digito)
print()
print(lista_nivel)


# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
def cargar_pokemones(pokemons):
    numero=int (input("ingrese un numero"))
    nombre=str (input("ingrese el nombre del pokemon"))
    tipo=str (input("ingrese el tipo del pokemon, para agregar otro tipo utilice la / "))
    nivel= int (input("ingrese el nivel del pokemon"))
    poke= {"numero":numero,"nombre":nombre,"tipo":tipo,"nivel":nivel}
    pokemons.append(poke)
    return()
cargar_pokemones(pokemons)


# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
print()
def ult_num(lista_ultimo_digito):
    print ("los pokemones que terminan en 1",lista_ultimo_digito[1])
    print()
    print ("los pokemones que terminan en 7",lista_ultimo_digito[7])
    print()
    print ("los pokemones que terminan en 9",lista_ultimo_digito[9])
    return()
ult_num(lista_ultimo_digito)


# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
print()
def pokes_multiplos(pokemons):
    multiplo2=[]
    multiplo5=[]
    multiplo10=[]
    for index,pokemon in enumerate(pokemons):
        num=pokemons[index]['nivel']
        if num%2==0:
            multiplo2.append(pokemons[index])
        if num%5==0:
            multiplo5.append(pokemons[index])
        if num%10==0:
            multiplo10.append(pokemons[index])
    print("los pokemones que son multiplo de 2 son",multiplo2)
    print()
    print("los pokemones que son multiplo de son 5",multiplo5)
    print()
    print("los pokemones que son multiplo de 10 son",multiplo10)
    return()
pokes_multiplos(pokemons)


# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
print()
def tipos(lista_tipo_poke):
    print("los pokemones de tipo acero son ",lista_tipo_poke["Acero"])
    print()
    print("los pokemones de tipo fuego son",lista_tipo_poke["Fuego"])
    print()
    print("los pokemones de tipo electrico son",lista_tipo_poke["Eléctrico"])
    print()
    print("los pokemones de tipo hielo son ",lista_tipo_poke["Hielo"])
    print()
    return()
tipos(lista_tipo_poke)


print(pokemons)