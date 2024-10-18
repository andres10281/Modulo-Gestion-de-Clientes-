clientes = {}

def menu_principal():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar Cliente")
        print("2. Iniciar Sesión")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su número de teléfono: ")

    if not nombre or not apellido or not correo or not telefono:
        print("\nError: Todos los campos son obligatorios. Intente nuevamente.")
        return

    clientes[correo] = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono
    }
    print("\nCliente registrado con éxito!")

def iniciar_sesion():
    correo = input("Ingrese su correo para iniciar sesión: ")
    telefono = input("Ingrese su número de teléfono como contraseña: ")

    if correo in clientes and clientes[correo]['telefono'] == telefono:
        print(f"\nInicio de sesión exitoso. Bienvenido/a {clientes[correo]['nombre']} {clientes[correo]['apellido']}!")
    else:
        print("\nError: Correo o número de teléfono incorrectos.")

def modificar_cliente():
    correo = input("Ingrese el correo del cliente que desea modificar: ")

    if correo not in clientes:
        print("\nError: Cliente no encontrado.")
        return

    print("\n¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Correo")
    print("4. Teléfono")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        if nuevo_nombre:
            clientes[correo]['nombre'] = nuevo_nombre
            print("\nNombre actualizado con éxito!")
    elif opcion == '2':
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        if nuevo_apellido:
            clientes[correo]['apellido'] = nuevo_apellido
            print("\nApellido actualizado con éxito!")
    elif opcion == '3':
        nuevo_correo = input("Ingrese el nuevo correo: ")
        if nuevo_correo and nuevo_correo not in clientes:
            clientes[nuevo_correo] = clientes.pop(correo)
            print("\nCorreo actualizado con éxito!")
        else:
            print("\nError: El correo ingresado ya existe o no es válido.")
    elif opcion == '4':
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        if nuevo_telefono:
            clientes[correo]['telefono'] = nuevo_telefono
            print("\nTeléfono actualizado con éxito!")
    else:
        print("\nOpción no válida. Intente nuevamente.")

def eliminar_cliente():
    correo = input("Ingrese el correo del cliente que desea eliminar: ")

    if correo in clientes:
        del clientes[correo]
        print("\nCliente eliminado con éxito!")
    else:
        print("\nError: Cliente no encontrado.")

if __name__ == "__main__":
    menu_principal()
