from tablero import Tablero
import os


EXTENSION = ".txt"
CARPETA_DATA = "data"
CARPETA_CONFIG = "config"
class DCCasillas:
    """Clase principal para el juego DCCasillas."""

    def __init__(self, usuario: str, config: str) -> None:
        """Inicializa una instancia del juego"""
        self.usuario = usuario
        self.puntaje = 0
        self.tablero_actual = None
        self.tableros = []
        
        ruta = os.path.join(CARPETA_CONFIG, config)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
            nombres_tableros = lineas[1:]
            
            for nombre_tablero in nombres_tableros:
                tablero_juego = Tablero()
                tablero_juego.cargar_tablero(nombre_tablero)
                self.tableros.append(tablero_juego)

    def abrir_tablero(self, num_tablero: int) -> None:
        """Abre un tablero en especifico."""
        self.tablero_actual = num_tablero

    def guardar_estado(self) -> bool:
        """Guarda archivo en /data."""
        if len(self.tableros) == 0 or not os.path.exists(CARPETA_DATA):
            return False
        elif self.usuario == "":
            return False
        else:
            nombre_del_archivo = self.usuario + EXTENSION
            ruta = os.path.join(CARPETA_DATA, nombre_del_archivo)
            cantidad_tableros = len(self.tableros)
            with open(ruta, 'w', encoding='utf-8') as archivo:
                archivo.write(f"{cantidad_tableros}\n")
                for tablero_dcc in self.tableros:
                    archivo.write(f"{tablero_dcc.movimientos}\n")
                    cantidad_de_filas = len(tablero_dcc.tablero) - 1
                    cantidad_de_columnas = len(tablero_dcc.tablero[0]) - 1
                    archivo.write(f"{cantidad_de_filas} {cantidad_de_columnas}\n")
                    for fila in tablero_dcc.tablero:
                        fila_casillas = " ".join(fila)
                        archivo.write(fila_casillas + "\n")
            return True
    
    def recuperar_estado(self) -> bool:
       """Recupera el estado del juego a partir del archivo indicado con el nombre de usuario."""
       if self.usuario == "":
            return False
       else:
            nombre_txt = self.usuario + EXTENSION
            ruta = os.path.join(CARPETA_DATA, nombre_txt)
            if not os.path.exists(ruta):
                return False
            else:
                with open(ruta, "r", encoding="utf-8") as archivo_config:
                    lineas = archivo_config.readlines()
                lista_lectura = []
                for linea in lineas:
                    lista_lectura.append(linea.strip())

                cantidad_tableros = lista_lectura[0]
                tableros_recuperar = []
                contador_tableros_agregados = 0
                parametros_tablero = lista_lectura[1:]

                if not str(cantidad_tableros).isdigit():
                    return False
                if len(parametros_tablero) == 0 or len(parametros_tablero) < 2:
                    return False
                while int(cantidad_tableros) > contador_tableros_agregados:
                    puntaje = int(parametros_tablero[0].strip())
                    if puntaje < 0:
                        return False
                    self.puntaje += puntaje
                    tablero_logitudes_str = parametros_tablero[1].split()
                    fila_tablero = int(tablero_logitudes_str[0])
                    nuevo_tablero = Tablero()
                    nuevo_tablero.movimientos = puntaje
                    nuevo_tablero.tablero = []
                    contador_tableros_lineas = 0
                    for linea_tablero in parametros_tablero[2:]:
                        sublista = linea_tablero.split()
                        for casilla in sublista:
                            if casilla.startswith("X") or casilla.startswith(".") or casilla.isdigit():
                                pass
                            else:
                                return False
                        nuevo_tablero.tablero.append(sublista)
                        contador_tableros_lineas += 1
                        if contador_tableros_lineas >= fila_tablero + 1:
                            parametros_tablero = parametros_tablero[2 + (fila_tablero + 1):]
                            break
                    nuevo_tablero.validar()
                    tableros_recuperar.append(nuevo_tablero)
                    contador_tableros_agregados += 1
                
                self.tableros = tableros_recuperar
                return True