"""1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
manera inversa al que están cargados. Preferentemente la función solo debe tener un
parámetro que es la lista de elementos. """

listaprueba=[1,2,3,4,5,6,7,8,9,10]

def listarInversamente(lista):
    if (len(lista)-1) < 0:
        return 0
    else:
        print(lista[-1])
        return listarInversamente(lista[:-1])
        
listarInversamente(listaprueba)