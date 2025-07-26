

paises={"Mexico","Brasil","España","Canada","Canada"}
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#funciones u operaciones
paises.add("Mexico")
print(paises)

paises.pop()
print(paises)



#ejemplo crear un programa que solicite los email de los alumnos de la utd almacenar en una lista y 
#posteriormente mostrar en pantalla los correos sin duplicados
alumnos = set()
while True:
    correo = input("Ingrese el correo del alumno (o 'salir' para terminar): ")
    if correo.lower() == 'salir':
        break
    alumnos.add(correo)
    print(f"Correo '{correo}' agregado.")
    print("alumos hasta el momento:", alumnos)
    
