catalogo = {}


def agregar_elemento(catalogo):
    nombre = input("Nombre del videojuego: ")
    if nombre in catalogo:
        print(f"Ya existe un elemento llamado '{nombre}'.")
        return

    genero = input("Género: ")
    fecha = input("Año de lanzamiento: ")
    jugado = input("¿Ya lo jugaste? (s/n): ") == "s"

    catalogo[nombre] = {
        "genero": genero,
        "fecha": fecha,
        "jugado": jugado,
    }
    print(f"'{nombre}' agregado al catálogo.")


flag = True
while flag:
        opcion = input("BIENVENIDO A CATALOGO ARENAS RETRO \n"
                       "1. Ver todos los elementos del catalogo \n"
                       "2. Agregar un elemento nuevo al catalogo \n"
                       "3. Modificar un atributo de un elemento existente \n"
                       "4. Salir del programa\n "
                       "Que desea hacer? ")
        if opcion == "1":
            print("Ver catálogo ")
        elif opcion == "2":
            agregar_elemento(catalogo)
        elif opcion == "3":
            print("Modificar elemento ")
        elif opcion == "4":
            print("¡Hasta luego!")
            flag = False
        else:
            print("  ✗ Opción inválida. Ingresá un número entre 1 y 4.")
