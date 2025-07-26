"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""


paises=["Mexico","Brasil","","Canada","Eespaña"]
pais1={
    "nombre":"Mexico",
    "capital":"CDMX",
    "poblacion":120000000,
    "idioma":"Español",
    "status":True,
    }

pais2={
    "nombre":"Brasil",
    "capital":"Brasilia",
    "poblacion":140000000,
    "idioma":"Portugues",
    "status":True,
    }

pais3={
    "nombre":"Canada",
    "capital":"Ottawa",
    "poblacion":100000000,
    "idioma":["Ingles","frances"],
    "status":True,
    }

print(pais1)

for i in pais1:
    print(f"{i} : {pais1[i]}")

pais1["altitud"]=3000
for i in pais1:
    print(f"{i} : {pais1[i]}")
# Actualizar un elemento del diccionario
pais1.update({"altitud":2500})
for i in pais1:
    print(f"{i} : {pais1[i]}")
import os
os.system("cls")
# Eliminar un elemento del diccionario
pais1.pop("altitud")
for i in pais1:
    print(f"{i} : {pais1[i]}")

#quitar el ultimo elemento del diccionario
    pais1.popitem()
for i in pais1:
    print(f"{i} : {pais1[i]}")