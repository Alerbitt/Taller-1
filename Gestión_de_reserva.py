def reserva():
    print("Bienvenido al sistema de reservas de canchas")
    con = int(input("Ingrese el número de reservas que desea hacer: "))
    informacion = []  # Declarar una lista vacía para almacenar las reservaciones
    for i in range(con):
        nombre = input("Ingrese su nombre: ")
        dia = input("Ingrese el día de la reservación: ")
        hora_inicio = input("Ingrese la hora de inicio de la reserva: ")
        hora_final = input("Ingrese la hora a la que finaliza la reserva: ")
        arbitro = input("¿Requiere árbitro? (si/no): ")
        reservacion = [nombre, dia, hora_inicio, hora_final, arbitro]
        informacion.append(reservacion)  # Agregar la reservación a la lista
    print(informacion)

reserva()
