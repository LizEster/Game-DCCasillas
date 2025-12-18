from visualizador import imprimir_tablero
from copy import deepcopy
from random import randint
from os import path


CARPETA_CONFIG = "config"
class Tablero:
    """Clase para manejar un tablero de juego."""

    def __init__(self) -> None:
        """Inicializa el tablero."""
        self.tablero = []
        self.movimientos = 0
        self.estado = False

    def cargar_tablero(self, archivo: str) -> None:
        """Carga el tablero desde un archivo."""
        ruta = path.join(CARPETA_CONFIG, archivo)
        
        with open(ruta, "r", encoding="utf-8") as archivo_tablero:
            lineas = archivo_tablero.readlines()
            primera_linea = int((lineas[0].strip().split())[0])

            for indice_fila in range(1, primera_linea + 2):
                if indice_fila < len(lineas):
                    fila_elementos = lineas[indice_fila].strip().split()
                    fila_tablero = []
                    for elemento_casilla in fila_elementos:
                        fila_tablero.append(elemento_casilla)
                    self.tablero.append(fila_tablero)


    def mostrar_tablero(self) -> None:
        """Muestra el tablero y su contenido."""
        imprimir_tablero(self.tablero)

    def modificar_casilla(self, fila: int, columna: int) -> bool:
        """Modifica las casillas del tablero y retorna True, caso contrario retorna False."""
        if str(fila).isdigit() and str(columna).isdigit():
            limite_fila = len(self.tablero)
            limite_columna = len(self.tablero[0])
            if fila >= limite_fila or fila < 0:
                if columna >= limite_columna or columna < 0:
                    return False
        else:
            return False
        valor = str(self.tablero[fila][columna])
        if valor.isdigit():
            self.tablero[fila][columna] = "X" + valor
            self.movimientos += 1
            return True
        if valor.startswith("X") and valor[1:].isdigit():
            self.tablero[fila][columna] = valor[1:]
            self.movimientos += 1
            return True
        return False

    def validar(self) -> bool:
        """Retorna True si la solucion del tablero es valida, caso contrario retorna False."""
        validacion_horizontal = True
        for fila in self.tablero[:-1]:
            casilla_objetivo = fila[-1]
            if casilla_objetivo == ".":
                continue
            else:
                suma = 0
                for valor in fila[:-1]:
                    if valor.isdigit():
                        suma += int(valor)
                    else:
                        if valor.startswith("X") or valor == ".":
                            pass
                        else:
                            validacion_horizontal = False
                if casilla_objetivo.isdigit() and suma != int(casilla_objetivo):
                    validacion_horizontal = False
                    break

        validacion_vertical = True
        for columna in range(len(self.tablero[0]) - 1):
            casilla_objetivo = self.tablero[-1][columna]
            if casilla_objetivo == ".":
                continue
            else:
                suma = 0
                for fila in self.tablero[:-1]:
                    if columna >= len(fila):
                        continue
                    valor = fila[columna]
                    if valor.isdigit():
                        suma += int(valor)
                    else:
                        if valor.startswith("X") or valor == ".":
                            pass
                        else:
                            validacion_vertical = False
                if casilla_objetivo.isdigit() and suma != int(casilla_objetivo):
                    validacion_vertical = False
                    break
        if validacion_horizontal and validacion_vertical:
            self.estado = True
        
        return validacion_horizontal and validacion_vertical

    def encontrar_solucion(self):
        """Retorna una copia de la instancia tablero si encuentra una solucion a este, de lo contrario retorna None."""
        tablero_original = deepcopy(self.tablero)
        
        if self.validar():
            copia_tablero = Tablero()
            copia_tablero.tablero = deepcopy(self.tablero)
            copia_tablero.estado = True
            copia_tablero.movimientos = self.movimientos
            return copia_tablero
        
        else:
            fila_casillas_regulares = len(self.tablero) - 1
            columnas_casillas_regulares = len(self.tablero[0]) - 1
            posicion_casillas_regulares = []
            for fila in range(fila_casillas_regulares):
                for columna in range(columnas_casillas_regulares):  
                    valor = str(self.tablero[fila][columna])
                    if valor.isdigit():
                        posicion_casillas_regulares.append([fila, columna])  

            if len(posicion_casillas_regulares) == 0:
                    return None
            else:
                maximas_busquedas = 1000000
                contador = 0
                while maximas_busquedas >= contador:
                    copia_tablero = Tablero()
                    copia_tablero.tablero = deepcopy(tablero_original)
                    copia_tablero.estado = False
                    copia_tablero.movimientos = 0
                    contador += 1
                        
                    for posicion in posicion_casillas_regulares:
                        fila = posicion[0]
                        columna = posicion[1]
                        if randint(1, 2) == 1:
                            copia_tablero.modificar_casilla(fila, columna)
                    if copia_tablero.validar():
                        return copia_tablero
        return None
