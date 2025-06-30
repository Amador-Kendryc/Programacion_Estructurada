# Proyecto de gestión de películas
#pelicula={
#    "nombre": "",
#    "categoria": "",
#    "clasificacion": "",
#    "genero": "",
#   "idioma": ""
#}

peliculas = {}

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def crearPeliculas():
    borrarPantalla()
    print ("\n\t•.:: •Agregar• Películas•::.\n")
    pelicula = {}
    pelicula["nombre"] = input("Ingresa-el - nombre:•").upper().strip()
    pelicula["categoria"] = input("Ingresa la- categoría: •").upper().strip()
    pelicula["clasificacion"] = input("Ingresa-la-clasificación: -").upper().strip()
    pelicula["genero"] = input("Ingresa-el genero: ").upper().strip()
    pelicula["idioma"] = input("Ingresa el •1diomas.").upper().strip()
    # Agregar la película al diccionario global usando el nombre como clave
    peliculas[pelicula["nombre"]] = pelicula
    print("\n\t\t.:::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:::")

def borrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas para borrar.")
    else:
        nombre = input("\n\tIngresa el nombre de la película a borrar: ").upper().strip()
        if nombre in peliculas:
            respuesta = input(f"\n\t¿Estás seguro de que deseas borrar la película '{nombre}'? (S/N): ").upper().strip()
            if respuesta == 'S':
                del peliculas[nombre]
            print(f"\n\tLa película '{nombre}' ha sido borrada exitosamente.")
        else:
            print(f"\n\tNo se encontró la película '{nombre}'.")
    esperarTecla()

def mostrarPeliculas():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for nombre, atributos in peliculas.items():
            print(f"\tNombre: {nombre}")
            for atributo, valor in atributos.items():
                print(f"\t{atributo}: {valor}")
            print("\t-------------------------")
    esperarTecla()

def agregarCaracteristicas():
    borrarPantalla()
    print("\n\t•.:: •Agregar• Características•::.\n")
    nombre = input("Ingresa el nombre de la película a la que deseas agregar características: ").upper().strip()
    if nombre in peliculas:
        atributo = input("Ingresa el nombre del atributo a agregar: ").lower().strip()
        valor = input(f"Ingresa el valor para '{atributo}': ").upper().strip()
        peliculas[nombre][atributo] = valor
        print(f"\n\tEl atributo '{atributo}' ha sido agregado a la película '{nombre}'.")
    else:
        print(f"\n\tNo se encontró la película '{nombre}'.")
    esperarTecla()

def modificarCaracteristicas():
    borrarPantalla()
    print("\n\t•.:: •Modificar• Características•::.\n")
    mostrarPeliculas2()
    if input("¿Quieres modificar el nombre de una película? (S/N): ").upper().strip() == 'S':
        nombre_actual = input("Ingresa el nombre actual de la película: ").upper().strip()
        if nombre_actual in peliculas:
            nuevo_nombre = input("Ingresa el nuevo nombre de la película: ").upper().strip()
            peliculas[nuevo_nombre] = peliculas.pop(nombre_actual)
            print(f"\n\tEl nombre de la película ha sido modificado de '{nombre_actual}' a '{nuevo_nombre}'.")
        else:
            print(f"\n\tNo se encontró la película '{nombre_actual}'.")
    elif input("¿Quieres modificar la categoria de la pelicula? (S/N): ").upper().strip() == 'S':
        categoria_actual = input("Ingresa la categoría actual de la película: ").upper().strip()
        print(f"La categoria actual es: {categoria_actual}")
        nueva_categoria = input("Ingresa la nueva categoría de la película: ").upper().strip()
        for pelicula in peliculas.values():
            if pelicula.get("categoria", "") == categoria_actual:
                pelicula["categoria"] = nueva_categoria
        print(f"\n\tLa categoría de la película ha sido modificada de '{categoria_actual}' a '{nueva_categoria}'.")
    elif input("¿Quieres modificar la clasificacion de la pelicula? (S/N): ").upper().strip() == 'S':
        clasificacion_actual = input("Ingresa la clasificación actual de la película: ").upper().strip()
        print(f"La clasificacion actual es: {clasificacion_actual}")
        nueva_clasificacion = input("Ingresa la nueva clasificación de la película: ").upper().strip()
        for pelicula in peliculas.values():
            if pelicula.get("clasificacion", "") == clasificacion_actual:
                pelicula["clasificacion"] = nueva_clasificacion
        print(f"\n\tLa clasificación de la película ha sido modificada de '{clasificacion_actual}' a '{nueva_clasificacion}'.")
    elif input("¿Quieres modificar el genero de la pelicula? (S/N): ").upper().strip() == 'S':
        genero_actual = input("Ingresa el género actual de la película: ").upper().strip()
        print(f"El Genero actual es: {genero_actual}")
        nuevo_genero = input("Ingresa el nuevo género de la película: ").upper().strip()
        for pelicula in peliculas.values():
            if pelicula.get("genero", "") == genero_actual:
                pelicula["genero"] = nuevo_genero
        print(f"\n\tEl género de la película ha sido modificado de '{genero_actual}' a '{nuevo_genero}'.")   
    elif input("¿Quieres modificar el idioma de la pelicula? (S/N): ").upper().strip() == 'S':
        idioma_actual = input("Ingresa el idioma actual de la película: ").upper().strip()
        print(f"El idioma actual es: {idioma_actual}")
        nuevo_idioma = input("Ingresa el nuevo idioma de la película: ").upper().strip()
        for pelicula in peliculas.values():
            if pelicula.get("idioma", "") == idioma_actual:
                pelicula["idioma"] = nuevo_idioma
        print(f"\n\tEl idioma de la película ha sido modificado de '{idioma_actual}' a '{nuevo_idioma}'.")    

def borrarCaracteristica():
    borrarPantalla()
    print("\n\t•.:: •Borrar• Característica•::.\n")
    mostrarPeliculas2()
    nombre = input("Ingresa el nombre de la película a la que deseas borrar una característica: ").upper().strip()
    if nombre in peliculas:
        atributo = input("Ingresa el nombre del atributo a borrar: ").lower().strip()
        if atributo in peliculas[nombre]:
            del peliculas[nombre][atributo]
            print(f"\n\tEl atributo '{atributo}' ha sido borrado de la película '{nombre}'.")
        else:
            print(f"\n\tEl atributo '{atributo}' no existe en la película '{nombre}'.")
    else:
        print(f"\n\tNo se encontró la película '{nombre}'.")
    esperarTecla()

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...")

def mostrarPeliculas2():
    borrarPantalla()
    if not peliculas:
        print("\n\tNo hay películas registradas.")
    else:
        print("\n\t.:: Listado de Películas ::.\n")
        for nombre, atributos in peliculas.items():
            print(f"\tNombre: {nombre}")
            for atributo, valor in atributos.items():
                print(f"\t{atributo}: {valor}")            

def salir():
    borrarPantalla()
    print("\n\tSaliendo del programa...")
    esperarTecla()
    exit(0)