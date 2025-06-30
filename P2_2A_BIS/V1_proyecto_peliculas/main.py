
#crear un proecto de peliculas que permita agregar peliculas, mostrar peliculas, limpiar la lista de peliculas, mostrar peliculas del 1 al 4 y salir del programa
from peliculas import agregarPeliculas, mostrarPeliculas, mostrarUnaPorUna, mostrarDel1Al4, limpiarPeliculas, esperarTecla, buscarPelicula, modificarPelicula, borrarPelicula
import os

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    borrarPantalla()
    print("\n\t=== MENÚ DE PELÍCULAS ===")
    print("\t1. Agregar película")
    print("\t2. Mostrar películas (listado)")
    print("\t3. Mostrar películas una por una")
    print("\t4. Mostrar películas del 1 al 4")
    print("\t5. Limpiar lista de películas")
    print("\t6. Buscar película")
    print("\t7. modificar película")
    print("\t8. borrar película")
    print("\t9. Salir")

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
        buscarPelicula()
    elif opcion == '7':
        modificarPelicula()
    elif opcion == '8':
        borrarPelicula()
    elif opcion == '9':
        print("\n\tSaliendo del programa...")
        break
    else:
        print("\n\tOpción no válida.")
        esperarTecla()
