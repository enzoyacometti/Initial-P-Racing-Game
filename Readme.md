# Tarea 1: Initial P :school_satchel:

## Consideraciones generales :octocat:

* El programa corre bien e implementé __todas__ las funcionalidades mínimas, correrlo no debería ser problema.

* Se asume que los archivos CSV __están creados__ y ubicados en la misma carpeta que el programa.

* Modelé todos los menús como clases, sin embargo, no todas las opciones de cada menú se implementan en forma de métodos (queda a criterio del ayudante si cumple con lo pedido en el _bonus_), lo importante es que __todos los menús implementan las opciones pedidas__ y son __a prueba de errores__.

* Además, el archivo ```formulas.py``` contiene todas las fórmulas matemáticas pedidas en el enunciado.

* La dinámica de la carrera se lleva a cabo __en el mismo código del archivo ```main.py```__, mediante el uso de ```while```.

* El juego se guarda __ante cualquier__ cambio relevante (compra de vehículos, mejora de vehículos, término de carreras, etc...).

* El manejo de los datos __no funcionará__ si se cambian las columnas de los archivos CSV.

* **_IMPORTANTE_**: _La subclase ```PistaHelada``` posee el atributo ```self.rocas``` y la subclase ```PistaRocosa``` posee el atributo ```self.hielo```. Esto es __*sólo para fijar estos valores en 0*__ y no afecten el cálculo en las fórmulas._

* **¿Qué contiene cada archivo?**
  * ```main.py```: Módulo principal desde donde se corre el programa.
  * ```clases.py```: Módulo que contiene a ```Persona```, ```Vehiculo``` y ```Pista```, con las respectivas clases que heredan de cada una.
  * ```menus.py```: Módulo que contiene a ```Menu``` y todos los submenús que heredan de dicha clase madre.

  * ```formulas.py```: Módulo que contiene las fórmulas matemáticas pedidas en el enunciado.
  * ```funciones.py```: Módulo que contiene únicamente funciones implementadas para mejor funcionamiento del programa, se explicará cada una más adelante.
  * ```parametros.py```: Módulo que contiene los parámetros a ser usados por el programa (los cuales no varían).

#### Archivo ```clases.py```
Como se observa en el diagrama, todo gira en torno a la clase abstracta ```Menu```, dentro de la cual se instancian personas de distintos tipos, además de ser la clase madre de todos los submenús del juego.

Las clases son las siguientes:
* ```Persona```:
    Como dice su nombre, representa a una persona, y como es clase abstracta no se puede instanciar, ya que se debe especificar si es un usuario o un contrincante.

    Posee los siguientes atributos:
    * nombre: ```str```
    * experiencia: ```float```
    * equipo: ```str```
    * equilibrio: ```int```
    * contextura: ```int```
    * personalidad: ```str```
    * tiempo_vuelta: ```int```
    * tiempo_acum: ```int```
    * vehiculo_actual: ```Vehiculo```
        * ```Usuario```: 
            Posee los siguientes atributos:
            * dinero: ```int```
            * nuevo: ```bool```
            * pista_actual: ```Pista```

        * ```Contrincante```:
            Posee los siguientes atributos:
            * nivel: ```str```

* ```Vehículo```:
    Representa a los vehículos del juego, esta es una clase abstracta que no se debe instanciar sin especificar el tipo de vehículo que se desea crear.
    Posee los siguientes atributos:
    * nombre: ```str```
    * dueño: ```str```
    * categoría: ```str```
    * chasis: ```int```
    * carrocería: ```int```
    * ruedas: ```int```
    * peso: ```int```

    Posee los siguientes métodos (que agregarán valor a la característica correspondiente del vehículo específico):
    * ```mejorar_chasis()```
    * ```mejorar_carroceria()```
    * ```mejorar_ruedas()```

    Posee la siguiente property (de manera que el chasis no quede negativo cuando le llegue daño):
    * get/set: ```chasis_actual```

    De esta clase heredan las siguientes subclases:
    * ```Automovil```: posee el atributo "motor" y el método ```mejorar_motor()```.
    * ```Troncomovil```: posee el atributo "zapatillas" y el método ```mejorar_zapatillas()```.
    * ```Bicicleta```: posee el atributo "zapatillas" y el método ```mejorar_zapatillas()```.
    * ```Motocicleta```: posee el atributo "motor" y el método ```mejorar_motor()```.

* ```Menu```:
    Es la clase abstracta "madre" del juego, de la cual heredan todos los submenús.
    Posee el siguiente método:
    * ```validar_input(opcion, i, n)```: que recibe "opcion" y verifica que es un número entre "i" y "n".

    Es decir, valida el input entregado por el usuario dependiendo del menu en que se aplique.

    De esta clase heredan las siguientes subclases:
    * ```MenuInicio```: 

        Posee los siguientes métodos:
        * ```recibir_input()```: presenta el menu de inicio de sesión y deriva a la opción indicada por el usuario.
        * ```cargar_partida(username)```: recibe un nombre de usuario y busca la partida correspondiente, devolviendo un objeto ```Usuario```.
        * ```crear_partida()```: recibe un nombre de usuario y, en base a los parámetros seleccionados por el usuario, crea un objeto ```Usuario```.
    
    * ```MenuPrincipal```:

        Posee los siguientes métodos:
        * ```recibir_input()```: Muestra las opciones disponibles y devuelve una opción válida seleccionada por el usuario.
        * ```guardar_partida(jugador)```: Sobreescribe los datos del piloto y el estado del vehículo actual.
        * ```salir()```: Termina el juego.
        
        Y el siguiente atributo:
        * exit: ```bool```
    
    * ```MenuCompra```:

        Posee los siguientes métodos:
        * ```recibir_input()```: Muestra las opciones disponibles y también se encarga de la compra de un vehículo, se continuará mostrando hasta que el usuario ingrese 0.
        
        Y el siguiente atributo:
        * jugador: ```Jugador```

    * ```MenuPrep```:

        Posee los siguientes métodos:
        * ```recibir_input()```: Muestra las pistas disponibles y los vehículos que posee el ```Usuario``` para elegir, devuelve ambos objetos en una lista de largo 2.

        Y el siguiente atributo:
        * jugador: ```Jugador```

    * ```MenuCarrera```:

        Posee los siguientes métodos:
        * ```recibir_input()```: Muestra la opción de dar una vuelta o de entrar a los pits, y devuelve la opción del usuario (recordar que la carrera se desarrolla en el mismo código del archivo ```main.py```).

        Y los siguientes atributos:
        * jugador: ```Jugador```
        * pista: ```Pista```
    
    * ```MenuPits```:

        Posee los siguientes métodos:
        * ```recibir_input()```: Ofrece las mejoras para cada parte del vehículo actual.
        * ```arreglar_vehiculo()```: Devuelve el chasis del vehículo a su estado máximo.

        Y el siguiente atributo:
        * jugador: ```Jugador```

* ```Pista```:
    Representa todas las pistas del juego, es una clase abstracta y, por lo tanto, no instanciable sin especificar si es una pista de hielo, rocosa o suprema.
    Posee los siguientes atributos:
    * nombre: ```str```
    * tipo: ```str```
    * dificultad: ```int```
    * vueltas: ```int```
    * contrincantes: ```list```
    * largo: ```int```
    * vuelta_actual: ```int```
    * completo: ```bool```

    Y el siguiente método:
    * ```catacterizar(jugador)```: Define los contrincantes que tendrá la pista indicada (en el caso que el parámetro ```NUMERO_CONTRINCANTES``` es menor a la lista de contrincantes por defecto de la pista) y también le otorga los vehículos a cada contrincante.

    De esta clase heredan las siguientes subclases:
    * ```PistaHelada```: posee los atributos "hielo" y "rocas" (*)
    * ```PistaRocosa```: posee los atributos "hielo" y "rocas" (*)

    Y de ambas estas subclases, hereda una tercera (multiherencia):
    * ```PistaSuprema```: posee los atributos hielo y rocas

    (*): *Recordar que PistaHelada sólo tiene el atributo rocas para setearlo en 0, y lo mismo con PistaRocosa y su atributo hielo, de esta manera no influye el aporte de estas cualidades en el cálculo de las fórmulas matemáticas.*

#### Archivo ```funciones.py```
Compilación de funciones usadas a lo largo del programa, la función de cada una se presenta a continuación:

* __caracterizar(equipo)__: recibe un ```equipo``` y retorna un diccionario con la personalidad, contextura y equilibrio de un usuario perteneciente a dicho ```equipo```.
* __calcular_chasis(categoria)__: recibe ```categoria``` y retorna un valor entre ```MIN``` y ```MAX``` de ```chasis``` para alguien perteneciente a dicho ```categoria```.
* __calcular_carroceria(categoria)__: recibe ```categoria``` y retorna un valor entre ```MIN``` y ```MAX``` de ```carroceria``` para alguien perteneciente a dicho ```categoria```.
* __calcular_ruedas(categoria)__: recibe ```categoria``` y retorna un valor entre ```MIN``` y ```MAX``` de ```ruedas``` para alguien perteneciente a dicho ```categoria```.
* __calcular_motor_zapa(categoria)__: recibe ```categoria``` y retorna un valor entre ```MIN``` y ```MAX``` de ```motor``` (en caso de ```Vehiculo``` motorizado) o ```MIN``` y ```MAX``` de ```zapatillas``` (en caso de ```Vehiculo``` no motorizado) para alguien perteneciente a dicho ```categoria```.
* __calcular_peso(categoria)__: recibe ```categoria``` y retorna un valor entre ```MIN``` y ```MAX``` de ```peso``` para alguien perteneciente a dicho ```categoria```.
* __manejar_csv(path)__: recibe un ```path``` y retorna un diccionario con las características de todos los pilotos del archivo ```pilotos.csv```.
* __n_lineas(path)__: recibe un ```path``` y devuelve la cantidad de lineas del archivo.
* __leer_pistas(path)__: recibe un ```path``` y devuelve en una lista las pistas disponibles para correr.
* __leer_vehiculos(path, username)__: recibe un ```path``` y devuelve los vehículos que posee el usuario.
* __guardar(path, objeto, tipo)__: se le entrega un parámetro ```tipo``` que puede ser 'v' o 'p' dependiendo si se desea guardar al piloto o al vehículo actual, los cuales se ingresan en ```objeto``` y se guardan en ```path```.
* __accidentar(prob, personas, jugador)__: le aplica la probabilidad (```prob```) de tener un accidente al jugador y contrincantes (```personas```).
* __verificar_descalificados(contrincantes, posiciones)__: remueve a los descalificados de la lista ```posiciones``` de la carrera y los sitúa en otra lista. Ambas listas son retornadas.
* __nombre_valido(username)__: verifica que ```username``` sea alfanumérico (incluyendo espacios).
* __nombre_repetido(jugador, nombre)__: verifica que ```jugador``` no tiene un vehículo con el mismo ```nombre```.
* __validar_input(opcion, i, n)__: verifica que ```opcion``` sea un número entre "i" y "n". Análogo al funcionamiento del método homónimo de ```Menu```.


* **¿Cómo funciona el programa?**
  * El código de ```main.py``` consiste en cuatro secciones principales:
    * Desde __línea 12__: Se instancia ```MenuInicio``` y se dan las opciones solicitadas, devolviendo éste a un objeto de tipo ```Usuario```. 
    * Desde __línea 16__: Se otorga un vehículo a elección al jugador en caso de que se haya creado recién (dictado por su atributo "nuevo").
    * Desde __línea 59__: Se instancia ```MenuPrincipal``` y se entra al ```while``` que controla el flujo entre la carrera y el ```MenuCompra```.
    * Desde __línea 75__: Se entra a la carrera mediante un ```while``` que itera hasta que se complete la pista o el chasis del usuario colapse. También controla el flujo entre ```MenuCarrera``` y ```MenuPits```.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (POO)

* **Definición de clases**: Clases ```Vehiculo```, ```Pista``` y ```Persona``` se encuentran en ```clases.py```.
* **Relación entre clases**: 
  * _Clases Abstractas_: ```Vehiculo```, ```Pista``` y ```Persona``` son clases abstractas.
  * _Agregación_: ```Pista``` es una agregación de ```Persona```.
  * _Multiherencia_: ```PistaSuprema``` hereda de ```PistaHelada``` y de ```PistaRocosa```.
* **Cargar y guardar partidas**: ```MenuInicio``` se encarga de cargar partidas guardadas , con ayuda de las funciones ```manejar_csv()``` y ```guardar()``` del archivo ```funciones.py```.
* **Initial P**: 
  * _Crear partida_: Se crea la partida sin problemas.
  * _Pits_: Se agrega el tiempo a la siguiente vuelta y se mejora el vehículo a elección del usuario.
  * _Carrera_: 
    * Se imprime tabla con toda la información pedida
    * Se otorga recompensa al jugador si lidera una vuelta al circuito 
    * Se remueve a los contrincantes descalificados
    * Se pueden encontrar los cálculos de la velocidades en el archivo ```formulas.py```, donde ```calc_vel_rec()``` se encarga de la __velocidad recomendada__, ```calcular_velocidad_intencional``` se encarga de la __velocidad intencional__ y ```calcular_velocidad_real()``` se encarga de la __velocidad real__.
    * En el archivo ```formulas.py``` se encuentra ```calcular_hipotermia()```
    * En el archivo ```formulas.py``` se encuentra ```daño_recibido_cada_vuelta()```
    * En el archivo ```formulas.py``` se encuentra ```probabilidad_accidente()```
  * _Fin carrera_: Si el jugador gana la carrera, se le otorga __dinero y experiencia__ según las funciones ```dinero_ganador()``` y ```experiencia_recibida()```. Si un contrincante gana se le otorga __sólo experiencia__ según este última función. Por último, se imprime claramente al ganador en pantalla.
* **Consola**: Todos los menús muestran __todas las opciones pedidas__ y son __robustos__.
* **Archivos**: La función principal de archivos CSV es ```manejar_csv()```. Al comienzo de cada módulo se observa que se importa ```parametros.py``` con la abreviación ```p```.
* **Bonus: Buenas Prácticas**: Se definieron __todos__ los menús como clases, sin embargo, no todos los métodos de los menús son métodos, queda a criterio del ayudante el logro del bonus. También, se centralizan las fórmulas matemáticas en el módulo ```formulas.py```.
* **Bonus: Power-ups**: No implementado.

## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```main.py```. 
* El archivo ```parametros.py``` viene con los parámetros establecidos para obtener resultados decentes (se me quedó ```NUMERO_CONTRINCANTES``` fijado en 1, puedes cambiarlo al número que desees).


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```, ```choice```, ```uniform```.
2. ```math```: ```ceil()```, ```floor()```
3. ```collections```: ```defaultdict```
4.  ```abc```: ```ABC```, ```abstractmethod``` (_lo importé y no lo usé_), ```abstractproperty``` (_lo importé y no lo usé_)
5. ```beautifultable```: ```BeautifulTable```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos y consideraciones que realicé durante la tarea son los siguientes:

1. Los archivos CSV están __previamente creados y dentro de la carpeta__ que contiene al programa
2. Se guarda la partida cada vez que sucede un __cambio importante__ (compra vehículo, mejora vehículo, fin de carrera, etc...)
3. Si el jugador es descalificado de carrera, el ganador será __el contrincante encabezando__ y se le otorgará __sólo experiencia__ al ganar (ya que no poseen dinero).
4. Por enunciado, en pistas rocosas los tiempos de vuelta son __constantes__ (a menos que se mejore un componente del vehículo).
5. Se puede mejorar el vehículo de __manera ilimitada__ en los pits.

-------