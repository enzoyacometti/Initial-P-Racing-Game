from random import randint
from collections import defaultdict
from abc import ABC, abstractmethod, abstractproperty
import clases
import menus
import parametros as p
import funciones as func
import formulas as form
from beautifultable import BeautifulTable

# Se presenta el menu de inicio y se define al jugador (crear/cargar partida)
menu_inicio = menus.MenuInicio()
jugador = menu_inicio.recibir_input()

# Seleccionar primer vehiculo y guardarlo en vehiculos.csv...
if jugador.nuevo:
    print("\n¡Bienvenid@ " + str(jugador.nombre) + "!" + "\n")
    print("Selecciona tu primer vehículo (de parte de la casa):\n")
    print("[1] Automóvil\n[2] Troncomóvil\n[3] Motocicleta\n[4] Bicicleta\n")
    opcion = int(input("Escoge una opción: "))

    while not func.validar_input(opcion, 1, 4):
        opcion = input("Seleccione una opción válida: ")

    if opcion == 1:
        categoria = 'automóvil'
    elif opcion == 2:
        categoria = 'troncomóvil'
    elif opcion == 3:
        categoria = 'motocicleta'
    elif opcion == 4:
        categoria = 'bicicleta'
    nombre_vehiculo = input("¡Genial! Ahora nombra a tu vehículo: ")
    while not func.nombre_valido(nombre_vehiculo):
        nombre_vehiculo = input("Escoge un nombre válido: ")

    if opcion == 1:
        jugador.vehiculo_actual = clases.Automovil(nombre_vehiculo, \
            jugador.nombre, categoria, func.calcular_chasis(categoria), \
                func.calcular_carrocería(categoria), func.calcular_ruedas(categoria), \
                    func.calcular_peso(categoria), func.calcular_motor_zapa(categoria))
    elif opcion == 2:
        jugador.vehiculo_actual = clases.Troncomovil(nombre_vehiculo, \
            jugador.nombre, categoria, func.calcular_chasis(categoria), \
                func.calcular_carrocería(categoria), func.calcular_ruedas(categoria), \
                    func.calcular_peso(categoria), func.calcular_motor_zapa(categoria))
    elif opcion == 3:
        jugador.vehiculo_actual = clases.Motocicleta(nombre_vehiculo, \
            jugador.nombre, categoria, func.calcular_chasis(categoria), \
                func.calcular_carrocería(categoria), func.calcular_ruedas(categoria), \
                    func.calcular_peso(categoria), func.calcular_motor_zapa(categoria))
    elif opcion == 4:
        jugador.vehiculo_actual = clases.Bicicleta(nombre_vehiculo, jugador.nombre, \
            categoria, func.calcular_chasis(categoria), func.calcular_carrocería(categoria), \
                func.calcular_ruedas(categoria), func.calcular_peso(categoria), \
                    func.calcular_motor_zapa(categoria))
    func.guardar(p.PATHS['VEHICULOS'], jugador.vehiculo_actual, 'v')
    func.guardar(p.PATHS['PILOTOS'], jugador, 'p')
    jugador.nuevo = False

# Se presenta el menu principal y se inicia la secuencia de juego...
menu_principal = menus.MenuPrincipal()
menu_principal.exit = False

# Se presenta el menu de preparación de carrera
# y se declara la pista y vehiculo que se usará...
while not menu_principal.exit:
    opcion = menu_principal.recibir_input()
    if opcion == 1:
        menu_prep = menus.MenuPrep(jugador)
        [jugador.pista_actual, jugador.vehiculo_actual] = \
            menu_prep.recibir_input(jugador, p.PATHS['PISTAS'])
        menu_carr = menus.MenuCarrera(jugador, jugador.pista_actual)
        print("\n¡COMIENZA LA CARRERA!\n")
        pits = False

        # Comienza la carrera hasta que se termine o el chasis del jugador se destruya
        while jugador.pista_actual.completo == False and jugador.vehiculo_actual.chasis_actual > 0:
            func.accidentar(form.probabilidad_accidente, \
                list([jugador] + jugador.pista_actual.contrincantes), jugador)
            jugador.vehiculo_actual.chasis_actual -= \
                form.daño_recibido_cada_vuelta(jugador.vehiculo_actual, jugador.pista_actual)
            for contrincante in jugador.pista_actual.contrincantes:
                contrincante.vehiculo_actual.chasis_actual -= \
                    form.daño_recibido_cada_vuelta(contrincante.vehiculo_actual, \
                        jugador.pista_actual)
                contrincante.tiempo_vuelta = form.tiempo_vuelta(contrincante, \
                    contrincante.vehiculo_actual, jugador.pista_actual, False)
                contrincante.tiempo_acum += contrincante.tiempo_vuelta
            jugador.tiempo_vuelta = form.tiempo_vuelta(jugador, jugador.vehiculo_actual, \
                jugador.pista_actual, pits)
            jugador.tiempo_acum += jugador.tiempo_vuelta
            pits = False
            posiciones = func.ordenar(jugador, jugador.pista_actual.contrincantes)
            if posiciones[0].nombre == jugador.nombre:
                recompensa = form.dinero_vuelta_x(jugador.pista_actual)
                jugador.dinero += recompensa
                print("\n", jugador.nombre, "va liderando y gana", recompensa, "pesos\n")
            [descalificados, posiciones] = \
                func.verificar_descalificados(jugador.pista_actual.contrincantes, posiciones)
            if form.daño_recibido_cada_vuelta(jugador.vehiculo_actual, jugador.pista_actual) > 0:
                print("\n¡Las rocas han dañado", \
                    form.daño_recibido_cada_vuelta(jugador.vehiculo_actual, \
                        jugador.pista_actual), "tu chasis!")
                print("Tu chasis queda en", jugador.vehiculo_actual.chasis_actual, "\n")
            print("\nVuelta: ", jugador.pista_actual.vuelta_actual, "/", \
                jugador.pista_actual.vueltas, "\n")
            v_base = form.calcular_velocidad_intencional(jugador, \
                jugador.vehiculo_actual, jugador.pista_actual)
            if jugador.vehiculo_actual.categoria == 'automóvil' or \
                jugador.vehiculo_actual.categoria == 'motocicleta':
                if int(form.calcular_velocidad_real(jugador, jugador.vehiculo_actual, \
                    jugador.pista_actual)) < int(v_base):
                    print("Debido a condiciones de la pista, tu velocidad ha sido afectada \
                        en " + str(int(form.calcular_velocidad_real(jugador, \
                            jugador.vehiculo_actual, jugador.pista_actual)) - int(v_base)) + "\n")
                else:
                    print("Tu velocidad no ha sido afectada durante la vuelta\n")
            elif jugador.vehiculo_actual.categoria == 'troncomóvil' or \
                jugador.vehiculo_actual.categoria == 'bicicleta':
                if int(form.calcular_velocidad_real(jugador, jugador.vehiculo_actual, \
                    jugador.pista_actual)) < int(v_base):
                    print("Debido a las condiciones de la pista, \
                        tu velocidad ha sido afectada en " + \
                            str(int(form.calcular_velocidad_real(jugador, \
                                jugador.vehiculo_actual, jugador.pista_actual)) \
                                    - int(v_base)) + "\n")
                else:
                    print("Tu velocidad no ha sido afectada durante la vuelta\n")
            print("Orden de los competidores:")
            table = BeautifulTable()
            table.column_headers = ["N°", "Nombre", "Vehículo", "T. Vuelta", \
                "T. Acumulado"]
            i = 1
            for persona in posiciones:
                table.append_row([i, persona.nombre, persona.vehiculo_actual.nombre, \
                    persona.tiempo_vuelta, persona.tiempo_acum])
                i += 1
            print(table)
            if len(descalificados) > 0:
                for persona in descalificados:
                    print("\n" + str(persona.nombre) + " queda fuera de la carrera...\n")
            if int(jugador.pista_actual.vuelta_actual) + 1 == int(jugador.pista_actual.vueltas):
                jugador.pista_actual.completo = True
            jugador.pista_actual.vuelta_actual += 1
            opcion_carrera = menu_carr.recibir_input()

            # Entrar a pits
            if opcion_carrera == 2:
                pits = True
                menu_pits = menus.MenuPits(jugador)
                tiempo_pits = form.tiempo_pits(jugador.vehiculo_actual)
                menu_pits.arreglar_vehiculo()
                opcion_pits = menu_pits.recibir_input()
                while opcion_pits != 0:
                    opcion_pits = menu_pits.recibir_input()
                func.guardar(p.PATHS['VEHICULOS'], jugador.vehiculo_actual, 'v')
        
        # Si vehículo se destruye, termina carrera
        if jugador.vehiculo_actual.chasis_actual == 0:
            print("¡Tu chasis ha colapsado!\n¡Pierdes la carrera!\n")
            jugador.vehiculo_actual.chasis_actual = int(jugador.vehiculo_actual.chasis)
            if len(posiciones) > 0:
                print(posiciones[0].nombre, "ha ganado la carrera")
                posiciones[0].experiencia += \
                    form.experiencia_recibida(posiciones[0], jugador.pista_actual, posiciones)
            else:
                print("¡¡Nadie ha terminado la carrera!!")

        # Si se dan todas las vueltas, termina carrera
        if jugador.pista_actual.completo == True:
            print("\nLa carrera ha terminado\n")
            print(table)
            jugador.vehiculo_actual.chasis_actual = int(jugador.vehiculo_actual.chasis)
            if posiciones[0] == jugador:
                jugador.dinero += form.dinero_ganador(jugador.pista_actual)
                print("\n", jugador.nombre, "ha ganado\n")
            else:
                print("\n", posiciones[0].nombre, "ha ganado\n")
            posiciones[0].experiencia += form.experiencia_recibida(posiciones[0], \
                jugador.pista_actual, posiciones)
            print("\n¡El dinero y la experiencia de victoria han sido asignad@s!\n\n")
            func.guardar(p.PATHS['VEHICULOS'], jugador.vehiculo_actual, 'v')
            func.guardar(p.PATHS['PILOTOS'], jugador, 'p')

    # Se presenta menu de compras
    elif opcion == 2:
        menu_compra = menus.MenuCompra(jugador)
        opcion_compra = menu_compra.recibir_input()
        while opcion_compra != 0:
            opcion_compra = menu_compra.recibir_input()

    # Se procede a guardar partida
    elif opcion == 3:
        menu_principal.guardar_partida(jugador)
        print("¡Partida guardada con éxito!")

    # Salir del juego
    elif opcion == 0:
        print("¡Hasta luego!...")
        menu_principal.salir()
