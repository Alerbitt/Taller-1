from Gestión_de_reserva import *
from Gestión_de_reportes import *
from Editar_datos_reserva import *
from Validación_de_usuarios import *

def mensajes():
    mensaje_menu_administrador = """
    1 Hacer reservas 
    2 Ver reportes 
    3 Gestionar horarios 
    4 Gestionar usuarios y contraseñas 
    5 Salir
    """
    mensaje_menu_responsable = """
    1 Hacer reservas
    2 Editar reservas
    3 Ver horarios 
    4 Salir
    """
    mensaje_menu_cliente = """
    1 Ver horario 
    2 Ver costo de las reservas y promociones
    3 Hacer reservas 
    4 Salir
    """
    return mensaje_menu_cliente, mensaje_menu_administrador, mensaje_menu_responsable

def menu_administrador():
    while True:
        _, mensaje_administrador, _ = mensajes()
        print(mensaje_administrador)
        opt_administrador = int(input("Seleccione una opción del menú: "))
        if opt_administrador == 1:
            hacer_reserva = reserva()
        elif opt_administrador == 2:
            menu_reportes()
        elif opt_administrador == 3:
            horario = editar_horario(dias_promocion)
        elif opt_administrador == 4:
            editar_usuarios()
        elif opt_administrador == 5:
            break
        else:
            print("Opción no contemplada en el menú. Inténtelo de nuevo.")

def menu_responsable():
    while True:
        _, _, mensaje_responsable = mensajes()
        print(mensaje_responsable)
        opt_responsable = int(input("Seleccione una opción del menú: "))
        if opt_responsable == 1:
            hacer_reserva = reserva()
        elif opt_responsable == 2:
            editar_reserva()
        elif opt_responsable == 3:
            dia, hora = horario_reservas()
            print("Los días para hacer las reservas son: ")
            for dia in dia:
                print(dia)
            print("Las horas para hacer las reservas son: ")
            for hora in hora:
                print(hora)
        elif opt_responsable == 4:
            break
        else:
            print("Opción no contemplada en el menú. Inténtelo de nuevo.")

def menu_cliente():
    while True:
        mensaje_cliente, _, _ = mensajes()
        print(mensaje_cliente)
        opt_cliente = int(input("Seleccione una opción del menú:\n "))
        if opt_cliente == 1:
            dia, hora = horario_reservas()
            print("Los días para hacer las reservas son: ")
            for dia in dia:
                print(dia)
            print("Las horas para hacer las reservas son: ")
            for hora in hora:
                print(hora)

        elif opt_cliente == 2:
            print("Los costos de las reservas son:\n ")
            print("Con árbitro 50.000 y sin árbitro 40.000\n")
            print("Los días de promociones son: ")
            mostrar_promociones()

        elif opt_cliente == 3:
            hacer_reserva = reserva()
        elif opt_cliente == 4:
            break
        else:
            print("Opción no contemplada en el menú. Inténtelo de nuevo.")
