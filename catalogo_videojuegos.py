import json
from utils import read_db, save_db 
DB_PATH = "catalogo.json"

catalogo = read_db(DB_PATH)





catalogo = {}

def ver_elementos(catalogo):
    if not catalogo:
        print("El catálogo está vacío.")
        return
    for nombre, atributos in catalogo.items():
        print(f"\n{nombre}")
        for clave, valor in atributos.items():
            print(f"  {clave}: {valor}")


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


def modificar_elemento(catalogo):
    nombre = input("Nombre del videojuego a modificar: ")
    if nombre not in catalogo:
        print(f"No existe un elemento llamado '{nombre}'.")
        return

    print(f"Atributos de '{nombre}': {catalogo[nombre]}")
    atributo = input("¿Qué atributo desea modificar? (genero/fecha/jugado): ")
    if atributo not in catalogo[nombre]:
        print(f"'{atributo}' no es un atributo válido.")
        return

    if atributo == "jugado":
        nuevo_valor = input("Nuevo valor (s/n): ") == "s"
    else:
        nuevo_valor = input("Nuevo valor: ")

    catalogo[nombre][atributo] = nuevo_valor
    print(f"'{atributo}' de '{nombre}' actualizado.")


flag = True
while flag:
        opcion = input("BIENVENIDO A CATALOGO ARENAS RETRO \n"
                       "1. Ver todos los elementos del catalogo \n"
                       "2. Agregar un elemento nuevo al catalogo \n"
                       "3. Modificar un atributo de un elemento existente \n"
                       "4. Salir del programa\n "
                       "Que desea hacer? ")
        if opcion == "1":
            ver_elementos(catalogo)
        elif opcion == "2":
            agregar_elemento(catalogo)
        elif opcion == "3":
            modificar_elemento(catalogo)
        elif opcion == "4":
            print("¡Hasta luego!")
            flag = False
        else:
            print("  ✗ Opción inválida. Ingresá un número entre 1 y 4.")



