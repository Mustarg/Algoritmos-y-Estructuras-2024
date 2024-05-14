"""El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro,
el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila."""

def usar_la_fuerza(mochila, indice=0):
    if (mochila[indice]=="Sable de luz") | (mochila[indice]=="sable de luz"):
        print("¡Dentro se encontro:",mochila[indice],"! Tras sacar ", indice ," objetos de la mochila \n¡Usas el sable para ayudarte a salir de los escombros!")
    else:
        if (indice==(len(mochila)-1)):
            print("Dentro se encontro: ", mochila[indice], "\n¡Pero no hay ni rastro del Sable de Luz en la mochila!\n(Que macana, espero que en este planeta no haya ratas come-jedi...)")
        else:
            print("Dentro se encontro: ", mochila[indice])
            return(usar_la_fuerza(mochila, indice+1))
        

mochila=[0,0,0,0,0]
for i in range(0, len(mochila)):
    mochila[i]=input("¿Que objetos desea guardar en su mochila para el siguiente viaje? "+str(i+1)+"/5: ")

#Los print siguientes tienen la unica finalidad de dar inmersion al codigo
#¡Si resultan molestos sientase libre de eliminarlos o marcarlos como comentario!.
print("¡Mochila equipada correctamente! Comenzando viaje hacia un planeta distante...")
print("*Sonidos de nave espacial*")
print("ERROR EN LOS SISTEMAS DE NAVEGACION")
print("*Sonido de choque*")
print("Te despiertas despues de que la nave se accidenta\ncontra el planeta, estas atrapado bajo escombros")
print("¡Afortunadamente tu mochila se encuentra en el suelo cerca tuyo!\nLa atraes usando la fuerza")    
usar_la_fuerza(mochila)
