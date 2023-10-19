

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

def editar_usuarios():
    # Mostrar usuarios y contraseñas actuales
    print("Usuarios y Contraseñas Actuales:")
    for usuario in usuarios:
        print(f"Usuario: {usuario[0]}, Contraseña: {usuario[1]}")

    opcion = input("¿Desea agregar un nuevo usuario? (si/no): ")
    if opcion.lower() == "si":
        nuevo_usuario = input("Introduzca el nombre de usuario: ")
        nueva_contraseña = int(input("Introduzca la nueva contraseña: "))
        usuarios.append([nuevo_usuario, nueva_contraseña])
        print("Usuario agregado exitosamente.")
    
    opcion = input("¿Desea editar un usuario existente? (si/no): ")
    if opcion.lower() == "si":
        nombre_usuario = input("Introduzca el nombre de usuario que desea editar: ")
        for usuario in usuarios:
            if usuario[0] == nombre_usuario:
                nueva_contraseña = int(input(f"Introduzca la nueva contraseña para {nombre_usuario}: "))
                usuario[1] = nueva_contraseña
                print("Contraseña actualizada exitosamente.")

    opcion = input("¿Desea eliminar un usuario? (si/no): ")
    if opcion.lower() == "si":
        nombre_usuario = input("Introduzca el nombre de usuario que desea eliminar: ")
        for usuario in usuarios:
            if usuario[0] == nombre_usuario:
                usuarios.remove(usuario)
                print(f"{nombre_usuario} eliminado exitosamente.")
    
    # Mostrar usuarios y contraseñas actualizadas
    print("Usuarios y Contraseñas Actualizados:")
    for usuario in usuarios:
        print(f"Usuario: {usuario[0]}, Contraseña: {usuario[1]}")