from Menu_usuarios import *
from Validación_de_usuarios import *

def menu():
    mensaje_principal ="""
    1. Administrador
    2. Responsable
    3. Cliente
    """
    print(mensaje_principal)
    return int(input("Seleccione una opción: "))

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
