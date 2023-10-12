# Funcion para dar mensajes 
from Validación_de_usuarios import *
from Gestión_de_reserva import reserva, horario_reservas
#from Gestión_de_reportes import 

def mensajes():
    mensaje_menu_principal =  """
    1. Administrador
    2. Responsable
    3. Cliente
    """
    mensaje_menu_administrador = """
    1 Hacer reservas 
    2 Ver reportes 
    3 Gestionar dias promocionales 
    4 Gestionar horarios 
    5 Gestionar usuarios y contraseñas 
    """
    mensaje_menu_responsable = """
    1 Ver reservas
    2 Editar reservas
    3 Ver horarios 
    """
    return mensaje_menu_principal, mensaje_menu_administrador, mensaje_menu_responsable

def menu():
    mensaje_principal, _ , _ = mensajes()
    print(mensaje_principal)
    return int(input("Seleccione una opción: "))

def menu_administrador():
    while True:
        _ , mensaje_administrador , _ = mensajes()
        print(mensaje_administrador)
        opt_administrador = int(input("Seleccione una opción del menú: "))
        if opt_administrador == 1:
            hacer_reserva = reserva()
        elif opt_administrador == 2:
            pass # Ver reportes
        elif opt_administrador == 3:
            pass # Gestionar dias promociones
        elif opt_administrador == 4:
            pass # Gestionar horario
        elif opt_administrador == 5:
            pass # Gestionar usuarios y contraseñas 
        else:
            pass # Mensaje de error

def menu_responsable():
    while True:
        _ , _ , mensaje_responsable = mensajes()
        print(mensaje_responsable)
        opt_responsable = int(input("Seleccione una opción del menú: "))
        if opt_responsable == 1:
            hacer_reserva = reserva()
        elif opt_responsable == 2:
            pass # Ver horario
        elif opt_responsable == 3:
            pass # Editar reservas 
        else:
            pass # Mensaje de error

def menu_cliente():
    while True:
        opt_cliente = int(input("Seleccione una opción del menú:\n "))
        if opt_cliente == 1:
            dias, horas_de_mañana, horas_de_tarde = horario_reservas()
            print(f"\nLos dias disponibles para hacer reservacion son:\n {dias}")
            print(f"\nLas horas disponibles para hacer resevaciones en la mañana son:\n {horas_de_mañana}")
            print(f"\nLas horas disponibles para hacer resevaciones en la tarde son:\n {horas_de_tarde}\n")
        elif opt_cliente == 2:
            hacer_reserva = reserva()
            print(hacer_reserva)
        elif opt_cliente == 3:
            pass

if __name__ == "__main__":
    while True:
        opt = menu()
        if opt == 1:
            comprobar_administrador = administrador()
            if comprobar_administrador:
                menu_administrador()
        elif opt == 2:
            comprobar_responsable = responsable()
            if comprobar_responsable:
                menu_responsable()
        elif opt == 3:
            menu_cliente()
        else:
            print("Opción no contemplada en el menú. Inténtelo de nuevo.")
