import funciones as func
import formulas as form
import parametros as p
from random import choice
from collections import defaultdict
from abc import ABC, abstractmethod, abstractproperty

class Persona(ABC):
    def __init__(self, nombre, experiencia, equipo, personalidad, contextura, equilibrio):
        self.nombre = nombre
        self.personalidad = personalidad
        self.contextura = int(contextura)
        self.equilibrio = int(equilibrio)
        self.experiencia = float(experiencia)
        self.equipo = equipo
        self.tiempo_vuelta = 0
        self.tiempo_acum = 0
        self.vehiculo_actual = None

class Usuario(Persona):
    def __init__(self, nombre, experiencia, equipo, personalidad, contextura, equilibrio, dinero):
        super().__init__(nombre, experiencia, equipo, personalidad, contextura, equilibrio)
        self.dinero = int(dinero)
        self.nuevo = None
        self.pista_actual = None

class Contrincante(Persona):
    def __init__(self, nombre, experiencia, equipo, personalidad, contextura, equilibrio, nivel):
        super().__init__(nombre, experiencia, equipo, personalidad, contextura, equilibrio)
        self.nivel = nivel

class Vehiculo(ABC):
    def __init__(self, nombre, dueño, categoria, chasis, carroceria, ruedas, peso):
        self.nombre = nombre
        self.dueño = dueño
        self.categoria = categoria
        self.chasis = int(chasis)
        self.carroceria = int(carroceria)
        self.ruedas = int(ruedas)
        self.peso = int(peso)
        self.__chasis_actual = int(chasis)

    @property
    def chasis_actual(self):
        return self.__chasis_actual
    
    @chasis_actual.setter
    def chasis_actual(self, d):
        if d < 0:
            self.__chasis_actual = 0
        else:
            self.__chasis_actual = d

    def mejorar_chasis(self):
        self.chasis *= int(p.MEJORAS['CHASIS']['EFECTO'])

    def mejorar_carroceria(self):
        self.carroceria *= int(p.MEJORAS['CARROCERIA']['EFECTO'])

    def mejorar_ruedas(self):
        self.ruedas *= int(p.MEJORAS['RUEDAS']['EFECTO'])

class Automovil(Vehiculo):
    def __init__(self, nombre, dueño, categoria, chasis, carroceria, ruedas, peso, motor):
        super().__init__(nombre, dueño, categoria, chasis, carroceria, ruedas, peso)
        self.motor = int(motor)

    def mejorar_motor(self):
        self.motor *= int(p.MEJORAS['MOTOR']['EFECTO'])

class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueño, categoria, chasis, carroceria, ruedas, peso, zapatillas):
        super().__init__(nombre, dueño, categoria, chasis, carroceria, ruedas, peso)
        self.zapatillas = int(zapatillas)
    
    def mejorar_zapatillas(self):
        self.zapatillas *= int(p.MEJORAS['ZAPATILLAS']['EFECTO'])

class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueño, categoria, chasis, carroceria, ruedas, peso, zapatillas):
        super().__init__(nombre, dueño, categoria, chasis, carroceria, ruedas, peso)
        self.zapatillas = int(zapatillas)

    def mejorar_zapatillas(self):
        self.zapatillas *= int(p.MEJORAS['ZAPATILLAS']['EFECTO'])
    
class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueño, categoria, chasis, carroceria, ruedas, peso, motor):
        super().__init__(nombre, dueño, categoria, chasis, carroceria, ruedas, peso)
        self.motor = int(motor)

    def mejorar_motor(self):
        self.motor *= int(p.MEJORAS['MOTOR']['EFECTO'])

class Pista(ABC):
    def __init__(self, nombre, tipo, dificultad, vueltas, contrincantes, largo):
        self.nombre = nombre
        self.tipo = tipo
        self.dificultad = int(dificultad)
        self.vueltas = int(vueltas)
        self.contrincantes = contrincantes
        self.largo = int(largo)
        self.vuelta_actual = 1
        self.completo = False
    
    def caracterizar(self, jugador):
        if len(self.contrincantes) > int(p.NUMERO_CONTRINCANTES):
            contrincantes = []
            for _ in range(0, p.NUMERO_CONTRINCANTES):
                contrincante = choice(self.contrincantes)
                contrincantes.append(contrincante)
                self.contrincantes.remove(contrincante)
            self.contrincantes = contrincantes
        cont = func.importar_contrincantes(self.contrincantes, p.PATHS['CONTRINCANTES'])
        self.contrincantes = []
        for c in cont:
            c = Contrincante(c[0], c[5], c[6], c[2], c[3], c[4], c[1])
            self.contrincantes.append(c)
        func.otorgar_vehiculos_cont(self.contrincantes, p.PATHS['VEHICULOS'])

class PistaHelada(Pista):
    def __init__(self, nombre, tipo, dificultad, vueltas, contrincantes, largo, hielo='', \
        **kwargs):
        super().__init__(nombre, tipo, dificultad, vueltas, contrincantes, largo, **kwargs)
        self.hielo = int(hielo)
        self.rocas = 0

class PistaRocosa(Pista):
    def __init__(self, nombre, tipo, dificultad, vueltas, contrincantes, largo, rocas='', \
        **kwargs):
        super().__init__(nombre, tipo, dificultad, vueltas, contrincantes, largo, **kwargs)
        self.rocas = int(rocas)
        self.hielo = 0

class PistaSuprema(PistaRocosa, PistaHelada):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
