#Desarrollar una función que permita convertir un número romano en un número decimal.
numerosRomanos={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500 , 'M':1000}

def conversorRomanoDecimal(numeroRomano, valor=0):
    if numeroRomano=="I":
        return 1
    else:
        if (valor==len(numeroRomano)-1):
            return numerosRomanos[numeroRomano[valor]]
        elif ((numeroRomano[valor]=='I') | (numeroRomano[valor]=='X') | (numeroRomano[valor]=='C')) & (numerosRomanos[numeroRomano[valor]]<numerosRomanos[numeroRomano[valor+1]]):
            return (conversorRomanoDecimal(numeroRomano, valor + 1)) - numerosRomanos[numeroRomano[valor]]
        else:
            return (conversorRomanoDecimal(numeroRomano, valor + 1) + numerosRomanos[numeroRomano[valor]])


num=input("Ingrese un numero romano(En mayusculas): ")
print("El numero convertido a decimal es: ", conversorRomanoDecimal(num))