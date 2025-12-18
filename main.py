from dccasillas import DCCasillas
from tablero import Tablero
import os


def mostrar_tablero(partida):
    print("______Mostrando Tablero_____")
    tablero_actual = partida.tableros[partida.tablero_actual]
    tablero_actual.mostrar_tablero()

def habilitar_deshabilitar_casillas(partida):
    tablero_actual = partida.tableros[partida.tablero_actual]
    fila = input("Ingrese un número de fila: ").strip()
    columna = input("Ingrese un número de columna: ").strip()
    if fila.isdigit() and columna.isdigit():
        casilla_modificada = tablero_actual.modificar_casilla(int(fila), int(columna))
        if casilla_modificada:
            print(f"Casilla ({fila}, {columna}) modificada :D")
            partida.puntaje += 1
            print("WOW se sumo tu puntaje.")
            print("\nEstado actual del tablero:")
            tablero_actual.mostrar_tablero()
        else:
            print(f"Error :( ... No se pudo modificar la casilla ({fila}, {columna}).")
            return partida
    else:
        print("Error :( ... Debe ingresar números válidos.")
        return partida
def verificar_solucion(partida):
    print("Verifiquemos tu tablero :D")
    tablero_actual = partida.tableros[partida.tablero_actual]
    es_solucion = tablero_actual.validar()
    if es_solucion:
        print("¡Felicidades! La solución es correcta <3")
        print(f"Tus movimientos realizados: {tablero_actual.movimientos}")
    else:
        print("La solución no es correcta aún. Sigue intentando :(")
        return partida
def encontrar_solucion(partida):
    print("Buscando solucion ...")
    tablero_actual = partida.tableros[partida.tablero_actual]
    solucion = tablero_actual.encontrar_solucion()
    if solucion:
        print("Este tablero tenia solucion :D")
        print("Tablero con la solución:")
        solucion.mostrar_tablero()
        filas_regulares = len(solucion.tablero) - 1
        columnas_regulares = len(solucion.tablero[0]) - 1
        puntos_ganados = filas_regulares * columnas_regulares
        partida.puntaje += puntos_ganados
        print(f"Has ganado {puntos_ganados} puntos!")
    else:
        print("No se pudo encontrar una solución para este tablero :(")
        return partida
    
def menu_acciones(partida):
    """Menú de acciones para jugar con los tableros"""
    opcion = ""
    while opcion != "5":
        print("\nDCCasillas")
        print(f"Usuario: {partida.usuario}, Puntaje: {partida.puntaje}")
        print(f"Número de tablero: {partida.tablero_actual} de {len(partida.tableros) - 1}")
        print(f"Movimientos tablero: {partida.tableros[partida.tablero_actual].movimientos}")
        print()
        print("*** Menú de Acciones ***")
        print()
        print("[1] Mostrar tablero")
        print("[2] Habilitar/deshabilitar casillas")
        print("[3] Verificar solución")
        print("[4] Encontrar solución")
        print("[5] Volver al menú de Juego")
        print()
        
        opcion = input("Indique su opción (1, 2, 3, 4, 5): ")
        
        if opcion == "1":
            mostrar_tablero(partida)
        elif opcion == "2":
            habilitar_deshabilitar_casillas(partida)
        elif opcion == "3":
            verificar_solucion(partida)
        elif opcion == "4":
            encontrar_solucion(partida)
        elif opcion == "5":
            print("\nVolviendo al menú de juego...\n")
            return partida
        else:
            print("\nOpción inválida, intente de nuevo.\n")
    return partida
def menu_juego(partida):
    print("¡Bienvenido a DCCasillas!\n")
    if partida != None and partida != "":
        print(f"Usuario: {partida.usuario}, Puntaje: {partida.puntaje}")
        resueltos = 0
        for tablero in partida.tableros:
                if tablero.estado:
                    resueltos = resueltos + 1
        print(f"Tableros resueltos: {resueltos} de {len(partida.tableros)}\n")
    else:
        print("Usuario: No definido, Puntaje: 0")
        print("Tableros resueltos: 0 de 0\n")
    print("*** Menú de Juego ***\n")
    print("[1] Iniciar juego nuevo")
    print("[2] Continuar juego")
    print("[3] Guardar estado de juego")
    print("[4] Recuperar estado de juego")
    print("[5] Salir del programa")
def iniciar_juego_nuevo(partida):
    if partida is not None and partida.usuario != "":
        usuario = partida.usuario
        opcion = input("\n ¿Desea cambiar su nombre de usuario?, Escriba si o no ... \n")
        if opcion.lower() == "si":
            usuario = input("Ingrese nombre de usuariol: ").strip()
            if usuario == "" or len(usuario) == 0:
                print("Error :( Debe ingresar un nombre de usuario válido.")
                return None
        elif opcion.lower() == "no":
            pass
        else:
            print("Error :( ... Debe ingresar si o no.")
    else:
        usuario = input("Ingrese nombre de usuario:").strip()
        if usuario == "" or len(usuario) == 0:
            print("Error :( ... Debe ingresar un nombre de usuario válido.")
            return None
    config = input("Ingrese nombre del archivo de configuración: ").strip()
    if config == "" or len(config) == 0:
        print("Error :( ... Debe ingresar un nombre de archivo válido.")
        return None
    if config.endswith(".txt"):
        archivo_usuario = config
    else:
        archivo_usuario = config + ".txt"
    ruta_config = os.path.join("config", archivo_usuario)
    if not os.path.exists(ruta_config):
        print(f"Error :( ... No se encontró el archivo de configuración {config}")
        return None
    nueva_partida = DCCasillas(usuario, archivo_usuario)
    if nueva_partida.tableros:
        nueva_partida.abrir_tablero(0)
        print("Comenzado nueva partida de DCCasillas :D")
        print("Pasando al Menú de Acciones...")
        menu_acciones(nueva_partida)
        return nueva_partida
    else:
        print("Error :( ... No se pudieron cargar los tableros.")
        return None
def continuar_juego(partida):
    if not partida or not partida.usuario:
        print("Error :( ... No hay usuario jugando todavia.")
        return None
    if partida.tablero_actual != None:
        print(f"Su tablero actual: {partida.tablero_actual}")
        opcion = input("¿Desea un nuevo número de tablero?, Escriba si o no ... \n")
        if opcion.lower() == "si":
            print(f"Tableros disponibles: 0 a {len(partida.tableros) - 1}")
            nuevo_tablero = input("Ingrese número de tablero: ").strip()
            if nuevo_tablero.isdigit():
                num_tablero = int(nuevo_tablero)
                if 0 <= num_tablero < len(partida.tableros):
                    partida.abrir_tablero(num_tablero)
                    print(f"Cambiando al tablero {num_tablero}...")
                    menu_acciones(partida)
                else:
                    print("Error :( ... Número de tablero inválido.")
                    return partida
            else:
                print("Error :( ... Debe ingresar un número válido.")
                return partida
        else:
            if partida.tablero_actual is not None:
                print(f"Continuando con tablero {partida.tablero_actual}...")
            else:
                partida.abrir_tablero(0)
                print("Continuando con tablero 0...")
    menu_acciones(partida)
    return partida
def guardar_estado_juego(partida):
    print("\nGuardando el estado del juego...\n")
    if not partida or not partida.usuario:
        print("Error :( ... No hay usuario definido. No se puede guardar estado de la partida del juego.")
        return menu_juego(partida)
    guardar_partida = partida.guardar_estado()
    if guardar_partida:
        print(f"Estado guardado en data/{partida.usuario}.txt")
    else:
        print("Error :( ... No se pudo guardar el estado del juego.")
def recuperar_estado_de_juego(partida):
    usuario = ""
    if partida and partida.usuario:
        usuario = partida.usuario
        usuario_actual = input(f"¿Quieres recuperar tu partida con tu nombre de usuario: '{usuario}'?, Escriba si o no ... \n").strip().lower()
        if usuario_actual.lower() != 'si':
            usuario = input("Ingrese nuevo nombre de usuario por favor: ").strip()
        else:
            print(f"Recuperando estado de {usuario}")
    else:
        usuario = input("Ingrese nombre de usuario para poder recuperar partida: ").strip()
    if not usuario:
        print("Error :( ... Debe ingresar un nombre de usuario válido.")
        return partida
    nombre_archivo = os.path.join("data", f"{usuario}.txt")
    if not os.path.exists(nombre_archivo):
        print(f"Error :( ... No se encontró el archivo {nombre_archivo}")
        return partida
    partida_recuperada = DCCasillas(usuario, "config.txt")
    partida_recuperada.usuario = usuario
    partida_recuperada.tableros = []
    partida_recuperada.puntaje = 0
    partida_recuperada.tablero_actual = 0
    
    recuperar_partida = partida_recuperada.recuperar_estado()
    
    if recuperar_partida == True:
        print(f"Estado recuperado desde {nombre_archivo}")
        return partida_recuperada
    else:
        print("Error :( ... No se pudo recuperar el estado del juego.")
        return partida

def main():
    partida = None
    opcion = ""
    while opcion != "5":

        menu_juego(partida)
        opcion = input("\nIndique su opción (1, 2, 3, 4, 5): ")

        if opcion == "1":
            print("\n Iniciando un juego nuevo...\n")
            nueva_partida = iniciar_juego_nuevo(partida)
            if nueva_partida:
                partida = nueva_partida
        elif opcion == "2":
            print("\n Continuando el juego...\n")
            partida = continuar_juego(partida)
        elif opcion == "3":
            print("\n Guardando el estado del juego...\n")
            guardar_estado_juego(partida)
        elif opcion == "4":
            print("\n Recuperando estado de juego...\n")
            partida_recuperada = recuperar_estado_de_juego(partida)
            if partida_recuperada:
                partida = partida_recuperada
        elif opcion == "5":
            print("\n Saliendo del programa...\n")
            print("\n Vuelva pronto viajer@ :D ...\n")
            break
        else:
            print("\n Opción inválida, intente de nuevo.\n")

if __name__ == "__main__":
    main()