def menu_principal():
    print("\n\t\t\t .:::Sistema de Gestión de Calificaciones :::.\n\t1.- Agregar \n\t2.- Mostrar\n\t3.- Calcular Promedios\n\t4.- SALIR")
    opcion=input("\n Elige una opción (1-4): ").upper().strip()

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cual tecla")

def agregar_calificaciones(lista): #parametro
    borrarPantalla()
    print("Agregar calificaciones")
    nombre=input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4): #esto lo hace tres veces, no esta recorriendo
        continua=True #salirme hasta que el valor est dentro del rango
        while continua:
            try:
            #calificaciones.append(float(input(f"Calificacion #{i}: ")))
                cal=float(input(f"Calificacion #{i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False#ya ingreso un valor permitido a ala lista pequeña
                else:
                    print("Ingresa una cal comprendida entre 0 y 10")
            except ValueError:
                print("Ingresa un valor numerico")

    lista.append([nombre]+calificaciones)#nombre lo convierte a lista, porque es lista con lista
    print("Accion realizada con exito")            

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar calificaciones")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calif.- 1':<10}{'Calif.- 2':<10}{'Calif.- 3':<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<15}")
        print("-"*60) 
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")   
    else: 
        print("No hay registros en el sistema")


def calcular_promedios(lista):
    borrarPantalla()
    print("Promedios de los alumnos")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=(fila[1]+fila[2]+fila[3])/3
            #promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio_grupal
        print("-"*40)
        promedio_grupal=promedio_grupal/len(lista) 
        print(f"El promedio grupal es de: {promedio_grupal}")   
    else: 
        print("No hay registros en el sistema")
#