
from Validación_de_usuarios import *

def menu():
    mensaje = """
    1. Administrador
    2. Responsable
    3. Cliente
    """
    print(mensaje)
    return int(input("Seleccione una opción: "))

def menu_administrador():
    while True:
        opt_administrador = int(input("Seleccione una opción del menú: "))
        if opt_administrador == 1:
            pass
        elif opt_administrador == 2:
            pass
        elif opt_administrador == 3:
            pass

def menu_responsable():
    while True:
        opt_responsable = int(input("Seleccione una opción del menú: "))
        if opt_responsable == 1:
            pass
        elif opt_responsable == 2:
            pass
        elif opt_responsable == 3:
            pass

def menu_cliente():
    while True:
        opt_cliente = int(input("Seleccione una opción del menú: "))
        if opt_cliente == 1:
            pass
        elif opt_cliente == 2:
            pass
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
