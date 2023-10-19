# funcion_reservas.py

def horario_reservas():
    dias = ["lunes", "jueves", "sabado", "domingo"]
    horas = ["(2:00 a 3:00)pm", "(3:00 a 4:00)pm", "(4:00 a 5:00)pm", "(5:00 a 6:00)pm", "(6:00 a 7:00)pm", "(7:00 a 8:00)pm"]
    return dias, horas

def promociones(dia):
    dias_promocion = ["lunes", "jueves"]
    return dia in dias_promocion

def calcular_precio(arbitro, hora, dia):
    precio_base = 40000
    precio_con_arbitro = 50000
    descuento_promocion = 0.15

    if arbitro == "si":
        if "am" in hora:
            precio = precio_con_arbitro
        else:
            precio = precio_base
    else:
        precio = precio_base

    if promociones(dia):
        precio *= (1 - descuento_promocion)
    return precio

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

def obtener_hora(horas_disponibles):
    while True:
        print("Escriba el número de la hora que desea registrar en el horario: ")
        for i, hora in enumerate(horas_disponibles, start=1):
            print(i, ":", hora)
        hora = int(input(" "))
        if 1 <= hora <= len(horas_disponibles):
            return horas_disponibles[hora - 1]
        print("Hora no válida. Por favor, elija una hora de la lista.")

def validar_arbitro():
    while True:
        arbitro = input("¿Requiere árbitro? (si/no): ")
        if arbitro == "si" or arbitro == "no":
            return arbitro
        else:
            print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")



