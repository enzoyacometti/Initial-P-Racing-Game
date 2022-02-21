import funciones as func
import formulas as form
import parametros as p
import clases
from random import choice
from collections import defaultdict
from abc import ABC


class Menu(ABC):
    def __init__(self):
        pass
    
    def validar_input(self, opcion, i, n):
        while len(opcion) > 1 or len(opcion) == 0 or ord(str(opcion)) < 48+int(i) \
            or ord(str(opcion)) > 48+int(n):
            opcion = input("Seleccione una opción válida: ")
        return int(opcion)

class MenuInicio(Menu):
    def __init__(self):
        super().__init__()
    
    def recibir_input(self):
        print("\n¡Bienvenido a Initial P!\n")
        print("[0] Crear partida\n[1] Cargar partida\n[2] Salir del Juego\n")
        opcion = self.validar_input(input("Seleccione una opción: "), 0, 2)
        if opcion == 0:
            return self.crear_partida()
        elif opcion == 1:
            username = input("\nEscriba un nombre de usuario: ")
            dic_pil = func.manejar_csv(p.PATHS['PILOTOS'])
            while not func.nombre_valido(username) or username not in dic_pil['Nombre']:
                username = input("Escriba un nombre de usuario valido: ")
            return self.cargar_partida(username)
        elif opcion == 2:
            exit()

    def cargar_partida(self, username):
        dic_pilotos = func.manejar_csv(p.PATHS['PILOTOS'])
        for i in range(0, len(dic_pilotos['Nombre'])):
            if dic_pilotos['Nombre'][i] == username:
                ii = i
        jugador = clases.Usuario(username, dic_pilotos['Experiencia'][ii], \
            dic_pilotos['Equipo'][ii], dic_pilotos['Personalidad'][ii], \
                dic_pilotos['Contextura'][ii], dic_pilotos['Equilibrio'][ii], \
                    dic_pilotos['Dinero'][ii])
        jugador.nuevo = False
        func.otorgar_vehiculos_cont([jugador], p.PATHS['VEHICULOS'])
        return jugador

    def crear_partida(self):
        username = input("Escriba un nombre de usuario: ")
        dic_pilotos = func.manejar_csv(p.PATHS['PILOTOS'])
        while not func.nombre_valido(username) or username in dic_pilotos['Nombre']:
            username = input("Escriba un nombre de usuario valido: ")
        print("\n¿A qué equipo desea pertenecer?\n")
        print("[1] Tareos\n[2] Híbridos\n[3] Docencios\n")
        equipo = self.validar_input(input("Seleccione una opción: "), 1, 3)
        while ord(str(equipo)) < 49 or ord(str(equipo)) > 51:
            equipo = input("Seleccione un número válido: ")
        if equipo == 1:
            equipo = 'Tareos'
        elif equipo == 2:
            equipo = 'Híbridos'
        elif equipo == 3:
            equipo = 'Docencios'
        dic_car = func.caracterizar(equipo)
        jugador = clases.Usuario(username, 0, equipo, dic_car['PERSONALIDAD'], \
            dic_car['CONTEXTURA'], dic_car['EQUILIBRIO'], p.DINERO_INICIAL)
        jugador.nuevo = True
        return jugador

class MenuPrincipal(Menu):
    def __init__(self):
        super().__init__()
        self.exit = None

    def recibir_input(self):
        print("\n-------MENU PRINCIPAL-------\n")
        print("[1] Iniciar carrera")
        print("[2] Comprar vehículos")
        print("[3] Guardar partida")
        print("[0] Salir del programa\n")
        return self.validar_input(input("Seleccione una opción: "), 0, 3)

    def guardar_partida(self, jugador):
        func.guardar(p.PATHS['PILOTOS'], jugador, 'p')
        func.guardar(p.PATHS['VEHICULOS'], jugador.vehiculo_actual, 'v')

    def salir(self):
        self.exit = True

class MenuCompra(Menu):
    def __init__(self, jugador):
        super().__init__()
        self.jugador = jugador

    def recibir_input(self):
        print("\n-------MENU DE COMPRAS-------\n")
        print("Dinero actual: " + str(self.jugador.dinero) + "\n")
        print("Vehículos disponibles para comprar:")
        print("[1] Automóvil - $" + str(p.PRECIOS['AUTOMOVIL']))
        print("[2] Troncomóvil - $" + str(p.PRECIOS['TRONCOMOVIL']))
        print("[3] Motocicleta - $" + str(p.PRECIOS['MOTOCICLETA']))
        print("[4] Bicicleta - $" + str(p.PRECIOS['BICICLETA']))
        print("-----------------------")
        print("[0] Regresar\n")
        opcion_compra = self.validar_input(input("Seleccione una opción: "), 0, 4)
        if opcion_compra == 0:
            return 0
        elif opcion_compra == 1:
            if self.jugador.dinero < p.PRECIOS['AUTOMOVIL']:
                print("¡¡No tiene suficiente dinero!!")
                return 1
            nombre = input("Escriba un nombre para su vehículo: ")
            while not func.nombre_valido(nombre) or func.nombre_repetido(self.jugador, nombre):
                nombre = input("El nombre no es válido o ya tiene un vehículo llamado así: ")
            self.jugador.dinero -= p.PRECIOS['AUTOMOVIL']
            categoria = "automóvil"
            vehiculo = clases.Automovil(nombre, self.jugador.nombre, categoria, \
                func.calcular_chasis(categoria), func.calcular_carrocería(categoria), \
                    func.calcular_ruedas(categoria), func.calcular_motor_zapa(categoria), \
                        func.calcular_peso(categoria))
            func.guardar(p.PATHS['VEHICULOS'], vehiculo, 'v')
            func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')
            print("¡Vehículo adquirido con éxito!\n")
            return 1
        elif opcion_compra == 2:
            if self.jugador.dinero < p.PRECIOS['TRONCOMOVIL']:
                print("¡¡No tiene suficiente dinero!!")
                return 2
            nombre = input("Escriba un nombre para su vehículo: ")
            while not func.nombre_valido(nombre) or func.nombre_repetido(self.jugador, nombre):
                nombre = input("El nombre no es válido o ya tiene un vehículo llamado así: ")
            self.jugador.dinero -= p.PRECIOS['TRONCOMOVIL']
            categoria = "troncomóvil"
            vehiculo = clases.Troncomovil(nombre, self.jugador.nombre, categoria, \
                func.calcular_chasis(categoria), func.calcular_carrocería(categoria), \
                    func.calcular_ruedas(categoria), func.calcular_peso(categoria), \
                        func.calcular_motor_zapa(categoria))
            func.guardar(p.PATHS['VEHICULOS'], vehiculo, 'v')
            func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')
            print("¡Vehículo adquirido con éxito!\n")
            return 2
        elif opcion_compra == 3:
            if self.jugador.dinero < p.PRECIOS['MOTOCICLETA']:
                print("¡¡No tiene suficiente dinero!!")
                return 3
            nombre = input("Escriba un nombre para su vehículo: ")
            while not func.nombre_valido(nombre) or func.nombre_repetido(self.jugador, nombre):
                nombre = input("El nombre no es válido o ya tiene un vehículo llamado así: ")
            self.jugador.dinero -= p.PRECIOS['MOTOCICLETA']
            categoria = "motocicleta"
            vehiculo = clases.Motocicleta(nombre, self.jugador.nombre, categoria, \
                func.calcular_chasis(categoria), func.calcular_carrocería(categoria), \
                    func.calcular_ruedas(categoria), func.calcular_motor_zapa(categoria), \
                        func.calcular_peso(categoria))
            func.guardar(p.PATHS['VEHICULOS'], vehiculo, 'v')
            func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')
            print("¡Vehículo adquirido con éxito!\n")
            return 3
        elif opcion_compra == 4:
            if self.jugador.dinero < p.PRECIOS['BICICLETA']:
                print("¡¡No tiene suficiente dinero!!")
                return 4
            nombre = input("Escriba un nombre para su vehículo: ")
            while not func.nombre_valido(nombre) or func.nombre_repetido(self.jugador, nombre):
                nombre = input("El nombre no es válido o ya tiene un vehículo llamado así: ")
            self.jugador.dinero -= p.PRECIOS['BICICLETA']
            categoria = "bicicleta"
            vehiculo = clases.Bicicleta(nombre, self.jugador.nombre, categoria, \
                func.calcular_chasis(categoria), func.calcular_carrocería(categoria), \
                    func.calcular_ruedas(categoria), func.calcular_motor_zapa(categoria), \
                        func.calcular_peso(categoria))
            func.guardar(p.PATHS['VEHICULOS'], vehiculo, 'v')
            func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')
            print("¡Vehículo adquirido con éxito!\n")
            return 4
        func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')

class MenuPrep(Menu):
    def __init__(self, jugador):
        super().__init__()
        self.jugador = jugador
    
    def recibir_input(self, jugador, path):
        print("Antes de empezar la carrera, debe elegir la pista:\n")
        n_lineas = func.n_lineas(path)
        pistas = func.leer_pistas(path)
        print("PISTAS DISPONIBLES:\n")
        i = 1
        for elemento in pistas:
            print("["+str(i)+"]", str(elemento.nombre))
            print("Tipo: " + str(elemento.tipo) + ",", "Dificultad: " + str(elemento.dificultad) \
                 + "\n")
            i += 1
        opcion = self.validar_input(input("Seleccione una opción: "), \
            0, n_lineas)
        pista = pistas[int(opcion) - 1]
        pista.caracterizar(jugador)
        vehiculos_disponibles = func.leer_vehiculos(p.PATHS['VEHICULOS'], jugador.nombre)
        print("\nAhora debe seleccionar cuál de sus vehículos desea usar:\n")
        print("VEHICULOS DISPONIBLES:\n")
        i = 1
        for vehiculo in vehiculos_disponibles:
            print("[" + str(i) + "]", vehiculo.nombre, "\n")
            print("Categoría:", vehiculo.categoria)
            print("Chasis:", vehiculo.chasis)
            print("Carrocería:", vehiculo.carroceria)
            print("Ruedas:", vehiculo.ruedas)
            if vehiculo.categoria == "automóvil" or vehiculo.categoria == "motocicleta":
                print("Motor:", vehiculo.motor)
            else:
                print("Zapatillas:", vehiculo.zapatillas)
            print("Peso:", vehiculo.peso, "\n")
            i += 1
        opcion = self.validar_input(input("Seleccione una opción: "), 1, \
            len(vehiculos_disponibles))
        vehiculo = vehiculos_disponibles[int(opcion) - 1]
        return [pista, vehiculo]

class MenuCarrera(Menu):
    def __init__(self, jugador, pista):
        super().__init__()
        self.jugador = jugador
        self.pista = pista
    
    def recibir_input(self):
        print("\n[1] Continuar carrera\n[2] Entrar a pits\n")
        return self.validar_input(input("Seleccione una opción: "), 1, 2)

class MenuPits(Menu):
    def __init__(self, jugador):
        super().__init__()
        self.jugador = jugador

    def arreglar_vehiculo(self):
        self.jugador.vehiculo_actual.chasis_actual = self.jugador.vehiculo_actual.chasis
        print("\n¡Vehículo reparado!")
        print("Ha tomado:", form.tiempo_pits(self.jugador.vehiculo_actual), "\n")
        self.jugador.tiempo_vuelta += form.tiempo_pits(self.jugador.vehiculo_actual)

    def recibir_input(self):
        print("\n----------Menu de Pits----------\n")
        print("Dinero actual:", self.jugador.dinero)
        print("Partes a mejorar:\n")
        print("[1] Chasis:", "x" + str(p.MEJORAS['CHASIS']['EFECTO']), "$" + \
            str(p.MEJORAS['CHASIS']['COSTO']))
        print("[2] Carrocería:", "x" + str(p.MEJORAS['CARROCERIA']['EFECTO']), "$" + \
            str(p.MEJORAS['CARROCERIA']['COSTO']))
        print("[3] Ruedas:", "x" + str(p.MEJORAS['RUEDAS']['EFECTO']), "$" + \
            str(p.MEJORAS['RUEDAS']['COSTO']))
        if self.jugador.vehiculo_actual.categoria == "automóvil" or \
            self.jugador.vehiculo_actual.categoria == "motocicleta":
            print("[4] Motor:", "x" + str(p.MEJORAS['MOTOR']['EFECTO']), "$" + \
                str(p.MEJORAS['MOTOR']['COSTO']) + "\n")
        else:
            print("[4] Zapatillas:", "x" + str(p.MEJORAS['ZAPATILLAS']['EFECTO']), "$" + \
                str(p.MEJORAS['ZAPATILLAS']['COSTO']) + "\n")
        opcion_pits = self.validar_input(input(\
            "Seleccione la parte que desea mejorar (0 para regresar): "), 0, 4)
        if opcion_pits == 1:
            if self.jugador.dinero > p.MEJORAS['CHASIS']['COSTO']:
                self.jugador.dinero -= p.MEJORAS['CHASIS']['COSTO']
                self.jugador.vehiculo_actual.mejorar_chasis()
        elif opcion_pits == 2:
            if self.jugador.dinero > p.MEJORAS['CARROCERIA']['COSTO']:
                self.jugador.dinero -= p.MEJORAS['CARROCERIA']['COSTO']
                self.jugador.vehiculo_actual.mejorar_carroceria()
        elif opcion_pits == 3:
            if self.jugador.dinero > p.MEJORAS['RUEDAS']['COSTO']:
                self.jugador.dinero -= p.MEJORAS['RUEDAS']['COSTO']
                self.jugador.vehiculo_actual.mejorar_ruedas()
        elif opcion_pits == 4:
            if self.jugador.vehiculo_actual.categoria == "automóvil" or \
                self.jugador.vehiculo_actual.categoria == "motocicleta":
                    if self.jugador.dinero > p.MEJORAS['MOTOR']['COSTO']:
                        self.jugador.dinero -= p.MEJORAS['MOTOR']['COSTO']
                        self.jugador.vehiculo_actual.mejorar_motor()
            else:
                if self.jugador.dinero > p.MEJORAS['ZAPATILLAS']['COSTO']:
                    self.jugador.dinero -= p.MEJORAS['ZAPATILLAS']['COSTO']
                    self.jugador.vehiculo_actual.mejorar_zapatillas()
        elif opcion_pits == 0:
            return 0
        func.guardar(p.PATHS['PILOTOS'], self.jugador, 'p')
    