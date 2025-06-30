# Proyecto de gestión de películas
peliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Películas ::.")
    nombre = input("Ingresa el nombre de la película: ").upper().strip()
    peliculas.append(nombre)
    print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::") 
    esperarTecla()

def mostrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for i, peli in enumerate(peliculas, start=1):
            print(f"\t{i}. {peli}")
    esperarTecla()

def mostrarUnaPorUna():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Mostrando películas una por una ::.\n")
        for i, peli in enumerate(peliculas, start=1):
            print(f"\tPelícula {i}: {peli}")
            input("\tPresiona Enter para ver la siguiente...")
    esperarTecla()

def mostrarDel1Al4():
    borrarPantalla()
    print("\n\t.:: Películas del 1 al 4 ::.\n")
    if len(peliculas) == 0:
        print("\tNo hay películas registradas.")
    else:
        for i in range(min(4, len(peliculas))):
            print(f"\t{i+1}. {peliculas[i]}")
    esperarTecla()

def limpiarPeliculas():
    borrarPantalla()
    confirmacion = input("¿Quieres limpiar la lista de películas? (s/n): ").strip().lower()
    if confirmacion == 's':
        peliculas.clear()
        print("\n\t::: ¡LA LISTA FUE LIMPIADA CON ÉXITO! :::")
    else:
        print("\n\t::: Operación cancelada :::")
    esperarTecla()

# Menú simple para probar las funciones

    while True:
        borrarPantalla()
        print("\n\t=== MENÚ DE PELÍCULAS ===")
        print("\t1. Agregar película")
        print("\t2. Mostrar películas (listado)")
        print("\t3. Mostrar películas una por una")
        print("\t4. Mostrar películas del 1 al 4")
        print("\t5. Limpiar lista de películas")
        print("\t6. Salir")

        opcion = input("\n\tSelecciona una opción: ")

        if opcion == '1':
            agregarPeliculas()
        elif opcion == '2':
            mostrarPeliculas()
        elif opcion == '3':
            mostrarUnaPorUna()
        elif opcion == '4':
            mostrarDel1Al4()
        elif opcion == '5':
            limpiarPeliculas()
        elif opcion == '6':
            print("\n\tSaliendo del programa...")
            break
        else:
            print("\n\tOpción no válida.")
            esperarTecla()

def buscarPelicula():
    nombre = nombre.lower().strip()
    """Busca una película por su nombre."""
    for peli in peliculas:
        if peli.lower() == nombre.lower():
            return peli
    return None
    if not (buscarPelicula in peliculas):
        print("\n\tNo se encontró la película.")
    else:
        print(f"\n\tPelícula encontrada: {buscarPelicula(nombre)}")
        print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def borrarPelicula():
    """Borra una película por su nombre."""
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
        esperarTecla()
        return
    
    nombre = input("Ingresa el nombre de la película a borrar: ").upper().strip()
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"\n\tPelícula borrada: {nombre}")
        print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        print("\n\tNo se encontró la película.")
    
    esperarTecla()

def modificarPelicula():



    """Modifica el nombre de una película."""
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
        esperarTecla()
        return
    
    nombre = input("Ingresa el nombre de la película a modificar: ").upper().strip()
    if nombre in peliculas:
        nuevo_nombre = input("Ingresa el nuevo nombre de la película: ").upper().strip()
        index = peliculas.index(nombre)
        peliculas[index] = nuevo_nombre
        print(f"\n\tPelícula modificada: {nuevo_nombre}")
        print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        print("\n\tNo se encontró la película.")
    
    esperarTecla()