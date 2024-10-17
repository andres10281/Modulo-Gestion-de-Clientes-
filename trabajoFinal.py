
clientes = {}

def menu_principal():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar Cliente")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su número de teléfono: ")

   
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


if __name__ == "__main__":
    menu_principal()
