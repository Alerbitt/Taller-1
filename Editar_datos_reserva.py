from Funciones_de_reserva import horario_reservas, promociones
dias_promocion = ["lunes", "jueves"]

def editar_horario(dias_promocion):
    dias, horas = horario_reservas()
    print("Días disponibles:")
    for i, dia in enumerate(dias, start=1):
        print(f"{i}. {dia}")
    print(f"{len(dias) + 1}. Editar días de promoción")
    print(f"{len(dias) + 2}. Editar horas de trabajo")
    print(f"{len(dias) + 3}. Regresar al menú principal")
    opcion = int(input("Seleccione una opción: "))

    if 1 <= opcion <= len(dias):
        nuevo_dia = input("Ingrese el nuevo día: ")
        if nuevo_dia not in dias:
            dias[opcion - 1] = nuevo_dia
            print("Día editado exitosamente.")
        else:
            print("El día ya está en la lista de días disponibles.")
        editar_horario(dias_promocion)
    elif opcion == len(dias) + 1:
        dias_promocion = editar_dias_promocion(dias_promocion)
        editar_horario(dias_promocion)
    elif opcion == len(dias) + 2:
        horas = editar_horas_trabajo(horas)
        editar_horario(dias_promocion)
    elif opcion == len(dias) + 3:
        return dias, horas, dias_promocion
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        editar_horario(dias_promocion)

def editar_dias_promocion(dias_promocion):
    print("Días de promoción actuales:", dias_promocion)
    print("Seleccione una opción:")
    print("1. Agregar día de promoción")
    print("2. Eliminar día de promoción")
    print("3. Regresar al menú de edición de horario")

    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "1":
        nuevo_dia = input("Ingrese el nuevo día de promoción: ")
        if nuevo_dia not in dias_promocion:
            dias_promocion.append(nuevo_dia)
            print("Día de promoción agregado exitosamente.")
        else:
            print("El día ya está en la lista de días de promoción.")
        return editar_dias_promocion(dias_promocion)
    elif opcion == "2":
        if not dias_promocion:
            print("No hay días de promoción para eliminar.")
        else:
            dia_a_eliminar = input("Ingrese el día que desea eliminar de promoción: ")
            if dia_a_eliminar in dias_promocion:
                dias_promocion.remove(dia_a_eliminar)
                print("Día de promoción eliminado exitosamente.")
            else:
                print("El día ingresado no está en la lista de días de promoción.")
        return editar_dias_promocion(dias_promocion)
    elif opcion == "3":
        return dias_promocion
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        return editar_dias_promocion(dias_promocion)

def editar_horas_trabajo(horas):
    print("Horas de trabajo actuales:")
    for i, hora in enumerate(horas, start=1):
        print(f"{i}. {hora}")
    print("0. Regresar al menú de edición de horario")
    opcion = int(input("Seleccione una opción: "))

    if 1 <= opcion <= len(horas):
        nueva_hora = input("Ingrese la nueva hora de trabajo: ")
        horas[opcion - 1] = nueva_hora
        print("Hora de trabajo editada exitosamente.")
        return editar_horas_trabajo(horas)
    elif opcion == 0:
        return horas
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        return editar_horas_trabajo(horas)
