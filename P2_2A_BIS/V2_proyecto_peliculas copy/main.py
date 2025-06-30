
#crear un proecto de peliculas que permita agregar peliculas, mostrar peliculas, limpiar la lista de peliculas, mostrar peliculas del 1 al 4 y salir del programa
#1-UTILIZAR FUNCIONES Y MANDAR LLAMAR DESDE OTRO ARCHIVO(MODULO)
#2-UTILIZAR DICTOS PARA ALMACENAR LAS ATRIBUTOS(NOMBRE, CATEGORIA, CLASIFICACION, GENERO, IDIOMA)
from peliculas import borrarPantalla, crearPeliculas, mostrarPeliculas, esperarTecla, borrarPeliculas, agregarCaracteristicas, modificarCaracteristicas, borrarCaracteristica, salir, mostrarPeliculas2
import os



while True:
    borrarPantalla()
    print("\n\t=== MENÚ DE PELÍCULAS ===")
    print("\t1. Agregar película")
    print("\t2. Borrar película")
    print("\t3. Mostrar películas (listado)")
    print("\t4. Agregar caracteristicas")
    print("\t5. Modificar caracteristicas")
    print("\t6. Borrar caracteristicas")
    print("\t7. Salir")

    opcion = input("\n\tSelecciona una opción: ")

    if opcion == '1':
        crearPeliculas()
    elif opcion == '2':
        borrarPeliculas()
    elif opcion == '3':
        mostrarPeliculas()
    elif opcion == '4':
        agregarCaracteristicas()
    elif opcion == '5':
        modificarCaracteristicas()
    elif opcion == '6':
        borrarCaracteristica()
    elif opcion == '7':
        salir()
        print("\n\tSaliendo del programa...")
        break
    else:
        print("\n\tOpción no válida.")
        esperarTecla()
