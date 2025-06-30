
# lista=[
#     ["Ruben",10.0,10.0,10.0],
#     ["Andres",8.0,9.5,6.8]
#     ]
#



#sistema de gestion de calificaciones con iconos que tenga agregar, mostrar, calcular promedios, buscar y salir

import os

# Diccionario para almacenar los estudiantes y sus calificaciones
estudiantes = {}

# Iconos para el menú
iconos = {
    "agregar": "📝",
    "mostrar": "👀",
    "promedio": "📊",
    "buscar": "🔍",
    "salir": "🚪"
}

def limpiar_pantalla():
    """Limpiar la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Mostrar el menú con iconos"""
    limpiar_pantalla()
    print("╔══════════════════════════════╗")
    print("║🏫SISTEMA DE GESTIÓN ESCOLAR🏫║")
    print("╠══════════════════════════════╣")
    print(f"║ 1. {iconos['agregar']} Agregar estudiante     ║")
    print(f"║ 2. {iconos['mostrar']} Mostrar calificaciones ║")
    print(f"║ 3. {iconos['promedio']} Calcular promedios     ║")
    print(f"║ 4. {iconos['buscar']} Buscar estudiante      ║")
    print(f"║ 5. {iconos['salir']} Salir                  ║")
    print("╚══════════════════════════════╝")

def agregar_estudiante():
    """Agregar un nuevo estudiante con sus calificaciones"""
    limpiar_pantalla()
    print("📝 AGREGAR ESTUDIANTE")
    print("════════════════════")
    
    nombre = input("Nombre del estudiante: ").strip().title()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return
    
    if nombre in estudiantes:
        print(f"⚠️ El estudiante {nombre} ya existe. ¿Deseas actualizar sus calificaciones? (s/n)")
        if input().lower() != 's':
            return
    
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"Ingrese la calificación {i}: "))
                calificaciones.append(cal)
                break
            except ValueError:
                print("❌ Error: Ingresa un número válido para la calificación.")

    estudiantes[nombre] = calificaciones
    print(f"✅ Estudiante {nombre} agregado/actualizado correctamente.")
    input("Presiona Enter para continuar...")

def mostrar_calificaciones():
    """Mostrar todas las calificaciones de los estudiantes"""
    limpiar_pantalla()
    print("👀 CALIFICACIONES DE ESTUDIANTES")
    print("═══════════════════════════════")
    
    if not estudiantes:
        print("📭 No hay estudiantes registrados.")
    else:
        for nombre, califs in estudiantes.items():
            print(f"📌 {nombre}: {', '.join(map(str, califs))}")
    
    input("\nPresiona Enter para continuar...")

def calcular_promedios():
    """Calcular y mostrar los promedios de todos los estudiantes"""
    limpiar_pantalla()
    print("📊 PROMEDIOS DE ESTUDIANTES")
    print("══════════════════════════")
    
    if not estudiantes:
        print("📭 No hay estudiantes registrados.")
    else:
        for nombre, califs in estudiantes.items():
            promedio = sum(califs) / len(califs)
            print(f"⭐ {nombre}: {promedio:.2f}")
            
        # Calcular promedio general
        todas_califs = [cal for califs in estudiantes.values() for cal in califs]
        promedio_general = sum(todas_califs) / len(todas_califs)
        print(f"\n🎯 Promedio general de la clase: {promedio_general:.2f}")
    
    input("\nPresiona Enter para continuar...")

def buscar_estudiante():
    """Buscar un estudiante y mostrar sus calificaciones y promedio"""
    limpiar_pantalla()
    print("🔍 BUSCAR ESTUDIANTE")
    print("═══════════════════")
    
    if not estudiantes:
        print("📭 No hay estudiantes registrados.")
        input("Presiona Enter para continuar...")
        return
    
    nombre = input("Nombre del estudiante a buscar: ").strip().title()
    
    if nombre in estudiantes:
        califs = estudiantes[nombre]
        promedio = sum(califs) / len(califs)
        print(f"\n📌 {nombre}:")
        print(f"   Calificaciones: {', '.join(map(str, califs))}")
        print(f"   Promedio: {promedio:.2f}")
    else:
        print(f"❌ No se encontró al estudiante {nombre}.")
    
    input("\nPresiona Enter para continuar...")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_calificaciones()
        elif opcion == '3':
            calcular_promedios()
        elif opcion == '4':
            buscar_estudiante()
        elif opcion == '5':
            print("\n🚪 Saliendo del sistema... ¡Hasta pronto! 👋")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()





        
