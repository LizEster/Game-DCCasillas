# Tarea 1: DCCasillas 4️⃣➕5️⃣🟰9️⃣
## Consideraciones Generales
En este trabajo se obtuvieron los **testcases públicos** de todos los ítems de la **parte 1** (automatización de `dccasillas.py` y `tablero.py`).  
Por otro lado, la **parte 2** que corresponde a los menús en `main.py`, se logró realizar mediante la ejecución por consola de los objetivos pedidos en el enunciado de la Tarea 1.Además, personalmente se fue probando con prueba y error futuros *testcases*.  

---

### Cosas implementadas y no implementadas ✅ ❌

#### Parte 1 - Automatización `dccasillas.py` / `tablero.py`: 23 pts (41,8%)

##### ✅ `tablero.py`
- **inicializador:**  
  Se inicializó la clase Tablero, definiendo sus atributos principales: `tablero`, estado de validez del tablero actual y contador de movimientos ejecutados.  

- **cargar_tablero:**  
  Se implementó el módulo `os.path` para construir la ruta del archivo, asegurando la portabilidad.  
  El archivo se abre en modo lectura, se obtiene la primera línea que define el tamaño del tablero y, a partir de ahí, se van leyendo las filas para llenar `self.tablero`.  

- **mostrar_tablero:**  
  Se modularizó desde `visualizador.py` mediante la función `imprimir_tablero`.  

- **modificar_casillas:**  
  Los parámetros `(fila, columna)` recibidos fueron convertidos a `str` para corroborar que la coordenada no diera a las casillas objetivo.Una vez validado, se obtiene el valor actual de la casilla regular en esa posición y se modifica.  
  - Si la casilla es un número → se marca con una `"X"`.  
  - Si la casilla comienza con `"X"` seguido de un número → se restaura a su valor original.  
  En ambos casos, se incrementa el contador de movimientos y retorna `True`.  
  Si no cumple con ninguna de estas condiciones, retorna `False`.  

- **validar:**  
  Se revisa la suma de las casillas de cada fila y de cada columna por separado, comparándolas con la casilla objetivo.Para esto se utilizan banderas que inician en `True`.Si alguna suma no coincide con su casilla objetivo → la bandera cambia a `False` y se interrumpe el ciclo.Por consiguiente, si todas las sumas coinciden, el tablero es válido.Entonces, si tanto la validación horizontal como la vertical resultan correctas, se actualiza el atributo `estado` de la clase Tablero a `True` y se retorna `True`.  
  En caso contrario, se retorna `False` y no se cambia el estado.  

- **encontrar_solucion:**  
  Primero, usando el método `validar`, se verifica que el tablero tenga solución.  
  De ser así, se crea y retorna una copia del tablero.En caso contrario, se recorren las casillas regulares (todas menos las de objetivo) y se guardan sus coordenadas en una lista.Luego se verifica que la lista no esté vacía, de ser así retorna `None`.Si no está vacía, se define un número máximo de búsquedas (**1.000.000**).  
  En cada intento:  
  - Se crea una copia del tablero original.  
  - Por cada casilla regular, se decide aleatoriamente con un 50% de probabilidad (con `randint(1, 2)`) si se modifica o no.  
  - Al terminar, se valida el tablero resultante.  
    - Si es correcto → retorna la copia como solución.  
    - Si no → se continúa hasta agotar el número máximo de búsquedas.  



##### ✅ `dccasillas.py`
- **inicializador:**  
  Recibe como parámetros el usuario y el archivo de configuración `config`.  
  También se inicializan los atributos principales de la clase.  
  Luego se crea la ruta con la librería `os` y se abre el archivo de configuración en la carpeta `config`.  
  Se obtienen los nombres de los tableros definidos en él.  
  Entonces, por cada nombre de tablero encontrado se hace lo siguiente:  
  - Se crea una instancia de la clase Tablero.  
  - Se carga su contenido con el método `cargar_tablero`.  
  - Finalmente, se agrega a la lista `self.tableros`.  

- **abrir_tablero:**  
  Recibe como parámetro el número de tablero (`num_tablero`) y lo guarda en `self.tablero_actual`.  

- **guardar_estado:**  
  Guarda el estado actual del juego en un archivo dentro de la carpeta `data`.  
  - Verifica que exista al menos un tablero en `self.tableros`.  
  - Comprueba que la carpeta `data` exista en el proyecto.  
  - Verifica que el usuario no sea un string vacío.  
  Construye el nombre del archivo como `"usuario.txt"`.  
  Luego escribe la información del tablero como lo menciona el enunciado (3.4.2. Formato de guardado de tablero).  
  Si todo el proceso se realiza correctamente → retorna `True`.  
  Caso contrario, si ocurre algún problema de validación → retorna `False`.  

- **recuperar_estado:**  
  Permite restaurar un juego desde un archivo previamente guardado.  
  - Comprueba que el nombre del usuario no esté vacío.  
  - Construye la ruta del archivo con `usuario.txt` en la carpeta `data`.  
  - Si el archivo existe, lee todas las líneas, las limpia de espacios y obtiene la cantidad de tableros que deben recuperarse.  
  - Recorre los parámetros de cada tablero en el archivo.  
  - Una vez reconstruido, se llama al método `validar()` para actualizar el estado del tablero y se agrega a una lista de recuperación.  
  - Finalmente, cuando se procesan todos los tableros, se actualiza `self.tableros` con los tableros recuperados y se retorna.  

#### Parte 2 Menus `main.py`: 25 pts (45,5%)

##### ✅ Menú de Juego
El menú de juego funciona al buscar si ya hay un jugador actual.  
De lo contrario, por default la información del jugador comienza con:  
- nombre de usuario = `"no definido"`  
- puntaje = 0  
- tableros resueltos = 0 de 0  

Luego se tienen **5 opciones**, cada una con su función asignada:  
1. `iniciar_juego_nuevo`  
2. `continuar_juego`  
3. `guardar_estado_de_juego`  
4. `recuperar_estado_de_juego`  
5. `salir del programa`  

Dependiendo de lo que escoja el usuario, su información va cambiando (puntaje, nombre de tablero, etc.).  
Asimismo, para los *inputs* se tienen 2 posibles respuestas, que pueden ser `"si"` o `"no"`.  
Estos se controlan con `lower()`, que transforma cada input a minúscula (no se consideran tildes).  

---

##### ✅ Menú de Acciones
El menú de acciones funciona con la información de usuario ya cargada anteriormente en el menú de juego.  
Se tienen **5 opciones**, de las cuales 4 dependen de los métodos de la clase Tablero:  
1. `mostrar_tablero` → depende del método `mostrar_tablero`.  
2. `habilitar_deshabilitar_casillas` → depende del método `modificar_casillas`.  
3. `verificar_solucion` → depende del método `validar`.  
4. `encontrar_solucion` → depende de `encontrar_solucion` de la clase Tablero.  

De la misma forma que en el menú de juego, los inputs de opción se manejan con `"si"` o `"no"` mediante `lower()`.  

---

### Aspectos Generales: 7 pts (12,7%)
- ✅ **Modularización**  
- ✅ **PEP8**  

---

## Ejecución 💻
El módulo principal de la tarea a ejecutar es main.py en la consola. Además se deben tener los siguientes archivos adicionales:
 1. tablero.py en T1
 2. dccasillar.py en T1

---

## Librerías 📚
Librerías externas que utilicé:
 1. ```os```: ```path```
 2. ```copy```: ```deepcopy```
 3. ```random```: ```randint```

Librerias internas que utilice:
 1. ```visualizador```: ```imprimir_tablero```
 2. ```tablero```: ```Tablero```
 3. ```dccasillas```: ```Dccasillas```

---

## Supuestos y consideraciones adicionales 🤔
- La creacion de el metodo encontrar_solucion de tablero.py, se creo en base a un algoritmo llamado busqueda aleatoria, el cual crea distintos esceneario mediante el azar y cada escenario se prueba hasta dar con el que se busca, en este caso con la solucion del tablero, en mi codigo se uso random, con una probabilidad del 50% es decir fue recorrido casilla por casilla y arbitrariamente como al lanzar una moneda al aire, la casilla se modificaba o no, por lo que al terminar de iterar se comprobaba mendiante el metodo validar si ese tablero era o no valido.

---

## Referencias de código externo 📖
- https://docs.python.org/es/3.12/howto/unicode.html#reading-and-writing-unicode-data hace utf-8 y está implementado en el archivo tablero.py en las lineas 21 y esta implementado en el archivo dccasillas.py en las lineas 19, 42 y 64, codifica los caracteres en español.
- https://docs.python.org/es/3.12/library/copy.html hace copia de tablero y esta implementado en el archivo tablero.py en las lineas 108, 112 y 134,Una copia profunda (deep copy) construye un nuevo objeto compuesto y luego, recursivamente, inserta copias en él de los objetos encontrados en el original.
- https://stackoverflow.com/questions/34865409/python-and-random-randint hace uso de randint y esta implementado en el archivo tablero.py en las lineas 142, se usa como funcion de probabilidad.


# Actualizaciones Tarea

14/08 Se sube la tarea al Syllabus

16/08 - 19/08 Se creó el archivo .gitignore, incorporando los archivos a ignorar según lo solicitado en el enunciado. Además, se desarrolló tablero.py, donde se importó la librería os para asegurar la portabilidad y lectura de datos; en este archivo se inicializó la Clase Tablero, en el se implemento el metodo "cargar_tablero".Asimismo se desarrollo la dccasillas.py, donde se importó la librería os para asegurar la portabilidad y lectura de datos; en este archivo se inicializó la Clase Dccasillas, en se implemento el metodo "abrir_tablero".

19/08 Para el archivo tablero.py, se importo el modulo "visualizador" con la funcion "imprimir_tablero" por lo que se implemento el metodo "mostrar_tablero", tambien se desarrollo e implemento el metodo "modificar_casilla" y el metodo "validar".

21/08 Se creo el archivo main.py, con funciones para la creacion del menu, en el se importaron los modulos dccasillas y tablero.Tambien se implemento el metodo "guardar_estado" en dccasillas.py.Por ultimo, se actualizaron cambios pertinentes en metodos ya implementados.

24/08 Se completo el menu del juego y el menu de acciones del archivo main.py, tambien se implemento en tablero.py el metodo encontrar_solucion, asimismo en dccasillas se implemento el metodo recuperar_estado.

26/08 Actualizacion final del readme.
