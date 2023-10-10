

usuarios = [["alerbit", 123456], ["david", 654321]]

def administrador():
    nombre_administrador = input("Bienvenido, por favor introduzca su nombre de usuario: ")
    contraseña_administrador = int(input("Bienvenido, por favor introduzca su contraseña: "))

    if (nombre_administrador == usuarios[0][0] and contraseña_administrador == usuarios[0][1]):
        print("Bienvenido/a")
        return True
    else:
        print("Contraseña o nombre de usuario incorrecto. Inténtelo de nuevo.")
        return False

def responsable():
    nombre_responsable = input("Bienvenido, por favor introduzca su nombre de usuario: ")
    contraseña_responsable = int(input("Bienvenido, por favor introduzca su contraseña: "))

    if (nombre_responsable == usuarios[1][0] and contraseña_responsable == usuarios[1][1]):
        print("Bienvenido/a")
        return True
    else:
        print("Contraseña o nombre de usuario incorrecto. Inténtelo de nuevo.")
        return False
