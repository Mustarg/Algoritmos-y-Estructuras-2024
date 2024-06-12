from Pila import Stack

"""2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
a) Contar cuantas especies hay;
b) Determinar cuantos descubridores distintos hay;
c) Mostrar todos los dinosaurios que empiecen con T;
d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
"""

pilaDinos = Stack()
pilaAux = Stack()

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },
  ]

for dino in dinosaurios:
    pilaDinos.push(dino)

def contarCantidad(pila, filtro):
    lista_filtro=[]
    while pila.size() > 0:
        if (lista_filtro.count(pila.on_top()[filtro]) == 0):
            lista_filtro.append(pila.on_top()[filtro])
            pilaAux.push(pila.pop())
        else:
            pilaAux.push(pila.pop())
    return len(lista_filtro)

def acomodarPila(pila, pilaAux):
    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

def dinosauriosConT(pila):
    lista_dinos_conT=[]
    while pila.size() > 0:
        if pila.on_top()["nombre"].startswith(("T")):
            lista_dinos_conT.append(pila.on_top()["nombre"])
            pilaAux.push(pila.pop())
        else:
            pilaAux.push(pila.pop())
    return lista_dinos_conT

def dinosauriosLivianos(pila): #están chiquitos
    lista_dinos_livianos=[]
    while pila.size() > 0:
        if (int(pila.on_top()["peso"]) < 275):
            lista_dinos_livianos.append(pila.on_top())
            pilaAux.push(pila.pop())
        else:
            pilaAux.push(pila.pop())
    return lista_dinos_livianos

def dinosauriosConAQS(pila):
    while pila.size() > 0:
        if pila.on_top()["nombre"].startswith(("A", "Q", "S")):
            pilaAux.push(pila.pop())
        else:
            pila.pop()

print("Hay un total de ",contarCantidad(pilaDinos, "especie"), " especies")
acomodarPila(pilaDinos, pilaAux)
print()
print("Hay un total de ",contarCantidad(pilaDinos, "descubridor"), " descubridores")
acomodarPila(pilaDinos, pilaAux)
print()
print("Los dinosaurios cuyos nombres comienzan con T son: ",dinosauriosConT(pilaDinos))
acomodarPila(pilaDinos, pilaAux)
print()
print("Los dinosaurios que pesan menos de 275 kilos son: ",dinosauriosLivianos(pilaDinos))
acomodarPila(pilaDinos, pilaAux)
print()
dinosauriosConAQS(pilaDinos)
print("Los dinosaurios cuyo nombre empieza con A, Q o S son: ", pilaAux.elements)