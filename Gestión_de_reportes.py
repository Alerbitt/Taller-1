from Validación_de_usuarios import usuarios
from Gestión_de_reserva import *


def mostrar_reservas_por_cancha(canchas_reserva):
    print("Reservas en la Cancha 1:")
    for reserva in canchas_reserva[0]:
        print(f"Nombre: {reserva[0]}, Día: {reserva[3]}, Hora: {reserva[4]}, Árbitro: {reserva[5]}")
    
    print("\nReservas en la Cancha 2:")
    for reserva in canchas_reserva[1]:
        print(f"Nombre: {reserva[0]}, Día: {reserva[3]}, Hora: {reserva[4]}, Árbitro: {reserva[5]}")

def contar_arbitro(informacion):
    contador = 0
    for reserva in informacion:
        if reserva[5] == "si":
            contador += 1
    return contador

def mostrar_promociones():
    dias_promocion = ["lunes", "jueves"]
    print("Días de promoción:")
    for dia in dias_promocion:
        print(dia)

def calcular_ganancias(informacion_reservas):
    total_ganancias = 0
    for reserva in informacion_reservas:
        precio_reserva = reserva[6]
        total_ganancias += precio_reserva
    return total_ganancias


def menu_reportes():
    while True:
        print("Menú de Reportes")
        print("1. Reservas por Cancha")
        print("2. Contar Reservas con Árbitro")
        print("3. Días de Promoción")
        print("4. Calcular Ganancias")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_reservas_por_cancha(canchas_reserva)
        elif opcion == "2":
            cantidad_arbitros = contar_arbitro(informacion)
            print(f"Total de reservas con árbitro: {cantidad_arbitros}")
        elif opcion == "3":
            mostrar_promociones()
        elif opcion == "4":
            ganancias_totales = calcular_ganancias(informacion)
            print(f"Ganancias totales: ${ganancias_totales}")
        elif opcion == "5":
            break
        else:
            print("Opción no contemplada en el menú. Inténtelo de nuevo.")