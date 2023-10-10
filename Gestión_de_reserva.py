

#Terminado al 85% falta hacer validaciones 

def horario_reservas():
    dias = ["lunes", "jueves", "sabado", "domingo"]
    horas_de_mañana = ["(9:00 a 10:00)am", "(10:00 a 11:00)am"]
    horas_de_tarde = ["(12:00 a 1:00)pm", "(1:00 a 2:00)pm", "(2:00 a 3:00)pm", "(3:00 a 4:00)pm", "(4:00 a 5:00)pm", "(5:00 a 6:00)pm"]
    return dias, horas_de_mañana, horas_de_tarde

def promociones():# falta establecer el monto a descontar 
    dia = "lunes"
    dia_promociones = ["lunes", "jueves"]
    if dia in dia_promociones:
        print("Cuenta con descuento")
    else:
        print("No cuenta con descuento ")

def reserva():
    dias, horas_de_mañana, horas_de_tarde = horario_reservas()
    informacion = []  # Declar0 una lista vacía para almacenar las reservaciones

    print("Bienvenido/a al sistema de reservas de canchas")
    con = int(input("Ingrese el número de reservas que desea hacer: "))
    
    for i in range(con):
        nombre = input("Ingrese su nombre: ")
        identificacion = int(input("Ingrese su numero de identificacion: "))
        telefono = int(input("Ingrese un numero de contacto: "))
        
        print(f"Días disponibles para hacer reservas: {dias}")
        dia = input("Ingrese el día de la reservación: ")

        tiempo = input("Elija 1 para la reserva en la mañana o 2 para la tarde: ")

        if tiempo == '1':
            print(f"Horas disponibles para hacer reservas en la mañana: {horas_de_mañana}")
            hora = input("Escriba la hora que desea registrar tal como se muestra en el horario: ")
            if hora not in horas_de_mañana:
                print("Hora no válida. Por favor, elija una hora de la lista.")
                continue
        elif tiempo == '2':
            print(f"Horas disponibles para hacer reservas en la tarde: {horas_de_tarde}")
            hora = input("Escriba la hora que desea registrar tal como se muestra en el horario: ")
            if hora not in horas_de_tarde:
                print("Hora no válida. Por favor, elija una hora de la lista.")
                continue
        else:
            print("Opción no válida. Por favor, elija 1 para la mañana o 2 para la tarde.")
            continue

        arbitro = input("¿Requiere árbitro? (si/no): ")
        # Agregar validación para asegurarse de que 'arbitro' sea 'si' o 'no'

        informacion.append([nombre, identificacion, telefono, dia, hora, arbitro])  # Agregar la reservación a la lista

        # Agregar validación para asegurarse de que la hora y el día reservados estén disponibles

    return informacion

reserva()
