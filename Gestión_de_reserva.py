
#para mañana mejorar la forma de poner las horas 

def horario_reservas():
    dias = ["lunes", "jueves", "sabado", "domingo"]
    horas_de_mañana = ["(9:00 a 10:00)am", "(10:00 a 11:00)am"]
    horas_de_tarde = ["(12:00 a 1:00)pm", "(1:00 a 2:00)pm", "(2:00 a 3:00)pm", "(3:00 a 4:00)pm", "(4:00 a 5:00)pm", "(5:00 a 6:00)pm"]
    return dias, horas_de_mañana, horas_de_tarde

def promociones(dia):
    dias_promocion = ["lunes", "jueves"]
    return dia in dias_promocion

def contar_arbitro(informacion):
    contador = 0
    for reserva in informacion:
        if reserva[5] == "si":
            contador += 1
    return contador

def obtener_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    identificacion = int(input("Ingrese su número de identificación: "))
    telefono = int(input("Ingrese un número de contacto: "))
    return nombre, identificacion, telefono

def obtener_dia_valido(dias):
    while True:
        dia = input("Ingrese el día de la reservación: ")
        if dia in dias:
            return dia
        else:
            print("Día no válido. Por favor, elija un día de la lista.")

def obtener_tiempo_valido():
    while True:
        tiempo = input("Elija 1 para la reserva en la mañana o 2 para la tarde: ")
        if tiempo in ['1', '2']:
            return tiempo
        else:
            print("Opción no válida. Por favor, elija 1 para la mañana o 2 para la tarde.")

def obtener_hora_valida(horas_disponibles):
    while True:
        hora = input(f"Escriba la hora que desea registrar tal como se muestra en el horario: ")
        if hora in horas_disponibles:
            return hora
        else:
            print("Hora no válida. Por favor, elija una hora de la lista.")

def reserva():
    dias, horas_de_mañana, horas_de_tarde = horario_reservas() #Pasamos las variables con el horario
    informacion = []

    print("Bienvenido/a al sistema de reservas de canchas")
    con = int(input("Ingrese el número de reservas que desea hacer: "))

    for i in range(con):
        nombre, identificacion, telefono = obtener_datos_usuario() 
        
        print(f"Días disponibles para hacer reservas: {dias}")
        dia = obtener_dia_valido(dias)

        tiempo = obtener_tiempo_valido()

        if tiempo == '1':
            horas_disponibles = horas_de_mañana
        else:
            horas_disponibles = horas_de_tarde

        hora = obtener_hora_valida(horas_disponibles)

        arbitro = input("¿Requiere árbitro? (si/no): ")

        if arbitro != "si" and arbitro != "no":
            print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")
            continue

        informacion.append([nombre, identificacion, telefono, dia, hora, arbitro])

    return informacion

# Llamada a la función principal
#informacion_reservas = reserva()

# Llamada a la función de contar árbitros
#cantidad_arbitros = contar_arbitro(informacion_reservas)

# Llamada a la función de promociones
#tiene_promocion = promociones(informacion_reservas[0][3])  # Se usa el primer día registrado para verificar promociones

#print("Reservas registradas:")
#for reserva in informacion_reservas:
    #print(reserva)

#print(f"Total de reservas con árbitro: {cantidad_arbitros}")
#if tiene_promocion:
    #print("Cuenta con descuento")
#else:
    #print("No cuenta con descuento")
