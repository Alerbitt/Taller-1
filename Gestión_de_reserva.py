# Gestion_reservas.py
from Funciones_de_reserva import *

# Variables globales
informacion = []  # Lista para almacenar la información de las reservas
dias_reserva = [[] for _ in range(4)]  # Lista para almacenar las reservas por día
canchas_reserva = [[] for _ in range(2)]  # Lista para almacenar las reservas por cancha

def reserva():
    global informacion, dias_reserva, canchas_reserva

    dias, horas = horario_reservas()

    print("Bienvenido/a al sistema de reservas de canchas")
    con = int(input("Ingrese el número de reservas que desea hacer: "))

    for i in range(con):
        nombre, identificacion, telefono = obtener_datos_usuario()

        print(f"Días disponibles para hacer reservas: {dias}")
        dia = obtener_dia_valido(dias)

        hora = obtener_hora(horas)
        arbitro = validar_arbitro()
        precio = calcular_precio(arbitro, hora, dia)

        reserva = [nombre, identificacion, telefono, dia, hora, arbitro, precio]
        informacion.append(reserva)

        # Verificar si el día ya tiene reservas
        dia_index = dias.index(dia)
        dias_reserva[dia_index].append(reserva)

        # Pedir al usuario que elija una cancha
        while True:
            cancha = input("Elija una cancha (cancha1 o cancha2): ")
            if cancha in ["cancha1", "cancha2"]:
                cancha_index = 0 if cancha == "cancha1" else 1

                if hora in [reserva[4] for reserva in canchas_reserva[cancha_index]]:
                    print(f"La cancha {cancha} ya está reservada en esa hora.")
                else:
                    canchas_reserva[cancha_index].append(reserva)
                break
            else:
                print("Cancha no válida. Por favor, elija cancha1 o cancha2.")

    return informacion, dias_reserva, canchas_reserva

def editar_reserva():
    dias, horas = horario_reservas()
    global informacion, dias_reserva, canchas_reserva  # Declarar las variables globales

    print("Editar una reserva existente")

    identificacion = int(input("Ingrese su número de identificación para buscar su reserva: "))
    reserva_encontrada = None

    for reserva in informacion:
        if reserva[1] == identificacion:
            reserva_encontrada = reserva
            break

    if reserva_encontrada is not None:
        print("Reserva encontrada:")
        print("Nombre:", reserva_encontrada[0])
        print("Día:", reserva_encontrada[3])
        print("Hora:", reserva_encontrada[4])
        print("Árbitro:", reserva_encontrada[5])
        print("Precio:", reserva_encontrada[6])

        while True:
            print("¿Qué desea editar?")
            print("1. Día")
            print("2. Hora")
            print("3. Árbitro")
            print("4. Cancelar edición")

            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                nuevo_dia = obtener_dia_valido(dias)
                dia_index = dias.index(nuevo_dia)
                dias_reserva[dia_index].append(reserva_encontrada)
                dias_reserva[dias.index(reserva_encontrada[3])].remove(reserva_encontrada)
                reserva_encontrada[3] = nuevo_dia
                print("Día editado exitosamente.")

            elif opcion == "2":
                nueva_hora = obtener_hora(horas)
                reserva_encontrada[4] = nueva_hora
                for i, cancha_reserva in enumerate(canchas_reserva):
                    if reserva_encontrada in cancha_reserva:
                        canchas_reserva[i].remove(reserva_encontrada)
                        canchas_reserva[i].append(reserva_encontrada)
                print("Hora editada exitosamente.")

            elif opcion == "3":
                nuevo_arbitro = validar_arbitro()
                reserva_encontrada[5] = nuevo_arbitro
                print("Árbitro editado exitosamente.")

            elif opcion == "4":
                print("Edición cancelada.")
                break

            else:
                print("Opción no válida. Por favor, elija una opción válida.")

    else:
        print("Reserva no encontrada para el número de identificación proporcionado.")