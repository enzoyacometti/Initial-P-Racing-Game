# Explicación Diagrama de Clases

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
    * nombre: str
    * dueño:
    * categoría
    * chasis
    * carrocería
    * ruedas
    * peso

    Posee los siguientes métodos (que agregarán valor a la característica correspondiente del vehículo específico):
    * mejorar_chasis()
    * mejorar_carroceria()
    * mejorar_ruedas()

    Posee la siguiente property:
    * get/set: chasis_actual
    
    De manera que el chasis no quede negativo cuando le llegue daño.

    De esta clase heredan las siguientes subclases:
    * Automovil: posee el atributo motor y el método mejorar_motor()
    * Troncomovil: posee el atributo zapatillas y el método mejorar_zapatillas()
    * Bicicleta: posee el atributo zapatillas y el método mejorar_zapatillas()
    * Motocicleta: posee el atributo motor y el método mejorar_motor()

* Menu:
    Es la clase abstracta "madre" del juego, de la cual heredan todos los submenús.
    Posee el siguiente método:
    * validar_input()

    El cual valida el input entregado por el usuario dependiendo del menu en que se aplique.

    De esta clase heredan las siguientes subclases:
    * MenuInicio: 

        Posee los siguientes métodos:
        * recibir_input()
        * cargar_partida(username)
        * crear_partida()
    
    * MenuPrincipal:

        Posee los siguientes métodos:
        * recibir_input()
        * guardar_partida(jugador)
        * salir()
        
        Y el siguiente atributo:
        * exit: bool
    
    * MenuCompra:

        Posee los siguientes métodos:
        * recibir_input()
        
        Y el siguiente atributo:
        * jugador: Jugador[]

    * MenuPrep:

        Posee los siguientes métodos:
        * recibir_input()

        El cual retorna la pista y vehiculo que se usarán en la partida actual.

        Y el siguiente atributo:
        * jugador: Jugador[]

    * MenuCarrera:

        Posee los siguientes métodos:
        * recibir_input()

        Y los siguientes atributos:
        * jugador: Jugador[]
        * pista: Pista[]
    
    * MenuPits:

        Posee los siguientes métodos:
        * recibir_input()
        * arreglar_vehiculo()

        Y el siguiente atributo:
        * jugador: Jugador[]

* Pista:
    Representa todas las pistas del juego, es una clase abstracta y, por lo tanto, no instanciable sin especificar si es una pista de hielo, rocosa o suprema.
    Posee los siguientes atributos:
    * nombre
    * tipo
    * dificultad
    * vueltas
    * contrincantes
    * largo
    * vuelta_actual
    * completo

    Y el siguiente método:
    * catacterizar(jugador)

    De esta clase heredan las siguientes subclases:
    * PistaHelada: posee los atributos hielo y rocas (*)
    * PistaRocosa: posee los atributos hielo y rocas (*)

    Y de ambas estas subclases, hereda una tercera (multiherencia):
    * PistaSuprema: posee los atributos hielo y rocas

    (*): *Es relevante acotar que PistaHelada sólo tiene el atributo rocas para setearlo en 0, y lo mismo con PistaRocosa y su atributo hielo, de esta manera no influye el aporte de estas cualidades en el cálculo de las fórmulas matemáticas.*
    
    *Por otro lado, PistaSuprema tiene valores no nulos para ambos de estos atributos.*

## Relaciones entre clases

### Herencia
Es claro que los distintos tipos de vehículos: ```Automóvil```, ```Troncomóvil```, ```Motocicleta``` y ```Bicicleta``` heredan de una clase abstracta superior ```Vehículo``` (que no se debe instanciar), ya que todos comparten una lista considerable de atributos (chasis, ruedas, carrocería, peso).
Por otro lado, motor y zapatillas son únicos de cada vehículo específico, por lo que se agregan a las clases hijas independientemente.

Por otro lado, la ```PistaHelada``` y ```PistaRocosa``` heredan de la clase madre ```Pista```, y a su vez, ```PistaSuprema``` debe heredar de ```PistaHelada``` y ```PistaRocosa``` ya que posee todos los atributos de ambos (recordar que ```PistaHelada``` posee el atributo "rocas" sólo para fijarlo en 0 y facilitar los cálculos, y lo mismo con ```PistaRocosa``` y su atributo "hielo"). Aquí se aprecia multiherencia.

Por último, la clase madre ```Persona``` tiene como clases hijas: ```Usuario``` y ```Contrincante```, los cuales difieren en muy pocas cualidades y, por esto, es razonable usar herencia.

### Composición
El caso de ```Persona``` con respecto a ```Menu``` y el caso de ```Vehículo``` respecto a ```Persona``` son casos de composición, ya que para el primero, es imposible instanciar a una persona (ya sea ```Usuario``` o ```Contrincante```) sin antes instanciar a los menús del juego, ya que estos son los que mandan. Para el segundo caso, la situación es la misma, no se puede instanciar un ```Vehículo``` sin antes declarar a un dueño de este (es decir, una ```Persona```).

### Agregación
Se puede ver agregación para la clase ```Pista``` ya que sólo entrará a jugar un rol dentro de una carrera, cuando se relaciona con la clase ```Persona```, sin embargo, cuando se carece de una ```Pista``` no se ven afectadas las clases ```Usuario``` o ```Contrincante```.