from random import randint, choices, uniform
from collections import defaultdict
import parametros as p
import clases
import formulas as form

def caracterizar(equipo):
    dic_car = defaultdict(int)
    if equipo == 'Tareos':
        dic_car['PERSONALIDAD'] = p.EQUIPOS['TAREOS']['PERSONALIDAD']
        dic_car['CONTEXTURA'] += randint(p.EQUIPOS['TAREOS']['CONTEXTURA']['MIN'], \
            p.EQUIPOS['TAREOS']['CONTEXTURA']['MAX'])
        dic_car['EQUILIBRIO'] += randint(p.EQUIPOS['TAREOS']['EQUILIBRIO']['MIN'], \
            p.EQUIPOS['TAREOS']['EQUILIBRIO']['MAX'])
    elif equipo == 'Docencios':
        dic_car['PERSONALIDAD'] = p.EQUIPOS['DOCENCIOS']['PERSONALIDAD']
        dic_car['CONTEXTURA'] += randint(p.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MIN'], \
            p.EQUIPOS['DOCENCIOS']['CONTEXTURA']['MAX'])
        dic_car['EQUILIBRIO'] += randint(p.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN'], \
            p.EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MAX'])
    elif equipo == 'Híbridos':
        dic_car['PERSONALIDAD'] = p.EQUIPOS['HIBRIDOS']['PERSONALIDAD']
        dic_car['CONTEXTURA'] += randint(p.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MIN'], \
            p.EQUIPOS['HIBRIDOS']['CONTEXTURA']['MAX'])
        dic_car['EQUILIBRIO'] += randint(p.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MIN'], \
            p.EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MAX'])
    return dic_car

def calcular_chasis(categoria):
    if categoria == 'automóvil':
        return randint(p.AUTOMOVIL['CHASIS']['MIN'], p.AUTOMOVIL['CHASIS']['MAX'])
    elif categoria == 'troncomóvil':
        return randint(p.TRONCOMOVIL['CHASIS']['MIN'], p.TRONCOMOVIL['CHASIS']['MAX'])
    elif categoria == 'bicicleta':
        return randint(p.BICICLETA['CHASIS']['MIN'], p.BICICLETA['CHASIS']['MAX'])
    elif categoria == 'motocicleta':
        return randint(p.MOTOCICLETA['CHASIS']['MIN'], p.MOTOCICLETA['CHASIS']['MAX'])

def calcular_carrocería(categoria):
    if categoria == 'automóvil':
        return randint(p.AUTOMOVIL['CARROCERIA']['MIN'], p.AUTOMOVIL['CARROCERIA']['MAX'])
    elif categoria == 'troncomóvil':
        return randint(p.TRONCOMOVIL['CARROCERIA']['MIN'], p.TRONCOMOVIL['CARROCERIA']['MAX'])
    elif categoria == 'bicicleta':
        return randint(p.BICICLETA['CARROCERIA']['MIN'], p.BICICLETA['CARROCERIA']['MAX'])
    elif categoria == 'motocicleta':
        return randint(p.MOTOCICLETA['CARROCERIA']['MIN'], p.MOTOCICLETA['CARROCERIA']['MAX'])

def calcular_ruedas(categoria):
    if categoria == 'automóvil':
        return randint(p.AUTOMOVIL['RUEDAS']['MIN'], p.AUTOMOVIL['RUEDAS']['MAX'])
    elif categoria == 'troncomóvil':
        return randint(p.TRONCOMOVIL['RUEDAS']['MIN'], p.TRONCOMOVIL['RUEDAS']['MAX'])
    elif categoria == 'bicicleta':
        return randint(p.BICICLETA['RUEDAS']['MIN'], p.BICICLETA['RUEDAS']['MAX'])
    elif categoria == 'motocicleta':
        return randint(p.MOTOCICLETA['RUEDAS']['MIN'], p.MOTOCICLETA['RUEDAS']['MAX'])

def calcular_motor_zapa(categoria):
    if categoria == 'automóvil':
        return randint(p.AUTOMOVIL['MOTOR']['MIN'], p.AUTOMOVIL['MOTOR']['MAX'])
    elif categoria == 'troncomóvil':
        return randint(p.TRONCOMOVIL['ZAPATILLAS']['MIN'], p.TRONCOMOVIL['ZAPATILLAS']['MAX'])
    elif categoria == 'bicicleta':
        return randint(p.BICICLETA['ZAPATILLAS']['MIN'], p.BICICLETA['ZAPATILLAS']['MAX'])
    elif categoria == 'motocicleta':
        return randint(p.MOTOCICLETA['MOTOR']['MIN'], p.MOTOCICLETA['MOTOR']['MAX'])

def calcular_peso(categoria):
    if categoria == 'automóvil':
        return randint(p.AUTOMOVIL['PESO']['MIN'], p.AUTOMOVIL['PESO']['MAX'])
    elif categoria == 'troncomóvil':
        return randint(p.TRONCOMOVIL['PESO']['MIN'], p.TRONCOMOVIL['PESO']['MAX'])
    elif categoria == 'bicicleta':
        return randint(p.BICICLETA['PESO']['MIN'], p.BICICLETA['PESO']['MAX'])
    elif categoria == 'motocicleta':
        return randint(p.MOTOCICLETA['PESO']['MIN'], p.MOTOCICLETA['PESO']['MAX'])

def manejar_csv(path):
    with open(path, 'r', encoding='utf8') as archivo:
        cabecera = archivo.readline().strip().split(',')
        dic_pilotos = defaultdict(list)
        for linea in archivo:
            linea = linea.strip().split(',')
            for i in range(0, 7):
                dic_pilotos[cabecera[i]].append(linea[i])
    return dic_pilotos

def n_lineas(path):
    with open(path, 'r', encoding='utf8') as archivo:
        return int(len(archivo.readlines()))

def leer_pistas(path):
    pistas_disponibles = []
    with open(path, 'r', encoding="utf-8") as file:
        file.readline().strip().split(',')
        for linea in file:
            linea = linea.strip().split(',')
            contrincantes = linea[6].strip().split(';')
            if linea[1] == "pista hielo":
                pista = clases.PistaHelada(linea[0], linea[1], linea[4], linea[5], \
                    contrincantes, linea[7], linea[2])
            elif linea[1] == "pista rocosa":
                pista = clases.PistaRocosa(linea[0], linea[1], linea[4], linea[5], \
                    contrincantes, linea[7], linea[3])
            elif linea[1] == "pista suprema":
                pista = clases.PistaSuprema(nombre=linea[0], tipo=linea[1], \
                    hielo=linea[2], rocas=linea[3], dificultad=linea[4], vueltas=linea[5], \
                        contrincantes=contrincantes, largo=linea[7])
            pistas_disponibles.append(pista)
    return pistas_disponibles

def leer_vehiculos(path, username):
    vehiculos_disponibles = []
    ## cabecera
    with open(path, 'r', encoding="utf-8") as file:
        file.readline().strip().split(',')
        for linea in file:
            linea = linea.strip().split(',')
            if linea[1] == username:
                if linea[2] == 'automóvil':
                    vehiculos_disponibles.append(clases.Automovil(linea[0], linea[1], \
                        linea[2], linea[3], linea[4], linea[5], linea[7], linea[6]))
                elif linea[2] == 'motocicleta':
                    vehiculos_disponibles.append(clases.Motocicleta(linea[0], linea[1], \
                        linea[2], linea[3], linea[4], linea[5], linea[7], linea[6]))
                elif linea[2] == 'bicicleta':
                    vehiculos_disponibles.append(clases.Bicicleta(linea[0], linea[1], \
                        linea[2], linea[3], linea[4], linea[5], linea[7], linea[6]))
                elif linea[2] == 'troncomóvil':
                    vehiculos_disponibles.append(clases.Troncomovil(linea[0], linea[1], \
                        linea[2], linea[3], linea[4], linea[5], linea[7], linea[6]))
    return vehiculos_disponibles

def guardar(path, objeto, tipo):
    # crear funcion para sobre escribir pilotos y vehiculos
    l_aux = []
    if tipo == 'p':
        with open(path, 'r', encoding="utf-8") as file:
            cabecera = file.readline().strip().split(',')
            for linea in file:
                linea = linea.strip().split(',')
                if linea[0] != objeto.nombre:
                    l_aux.append(linea)
    # tengo lista de listas con las lineas del file original sin el jugador
        with open(path, 'w', encoding="utf-8") as file:
            file.write(str(",".join(cabecera)) + "\n")
            for elemento in l_aux:
                cosa = ",".join(elemento)
                file.write(str(cosa) + "\n")
            file.write(str(objeto.nombre) + "," + str(objeto.dinero) + "," + \
                str(objeto.personalidad) + "," + str(objeto.contextura) + "," + \
                    str(objeto.equilibrio) + "," + str(objeto.experiencia) + "," + \
                        str(objeto.equipo) + "\n")
    elif tipo == 'v':
        with open(path, 'r', encoding="utf-8") as file:
            cabecera = file.readline().strip().split(',')
            for linea in file:
                linea = linea.strip().split(',')
                if linea[0] != objeto.nombre:
                    l_aux.append(linea)
    # tengo lista de listas con las lineas del file original sin el vehiculo actual
        with open(path, 'w', encoding="utf-8") as file:
            file.write(str(",".join(cabecera)) + "\n")
            for elemento in l_aux:
                cosa = ",".join(elemento)
                file.write(str(cosa) + "\n")
            if objeto.categoria == "automóvil" or objeto.categoria == "motocicleta":
                file.write(objeto.nombre + "," + objeto.dueño + "," + objeto.categoria + "," + \
                    str(objeto.chasis) + "," + str(objeto.carroceria) + "," + str(objeto.ruedas) \
                        + "," + str(objeto.motor) + "," + str(objeto.peso) + "\n")
            elif objeto.categoria == "bicicleta" or objeto.categoria == "troncomóvil":
                file.write(objeto.nombre + "," + objeto.dueño + "," + objeto.categoria + "," + \
                    str(objeto.chasis) + "," + str(objeto.carroceria) + "," + str(objeto.ruedas) \
                        + "," + str(objeto.zapatillas) + "," + str(objeto.peso) + "\n")

def importar_contrincantes(lista_nombres, path):
    contrincantes = []
    con_final = []
    with open(path, 'r', encoding="utf-8") as file:
        file.readline().strip().split(',')
        for linea in file:
            linea = linea.strip().split(',')
            contrincantes.append(linea)
    for persona in contrincantes:
        for i in range(0, len(lista_nombres)):
            if persona[0] == lista_nombres[i]:
                con_final.append(persona)
    return con_final

def otorgar_vehiculos_cont(contrincantes, path_vehiculos):
    with open(path_vehiculos, 'r', encoding="utf-8") as file:
        file.readline().strip().split(',')
        for linea in file:
            linea = linea.strip().split(',')
            for c in contrincantes:
                if linea[1] == c.nombre:
                    categoria = linea[2]
                    if categoria == "automóvil":
                        c.vehiculo_actual = clases.Automovil(linea[0], linea[1], categoria, \
                            linea[3], linea[4], linea[5], linea[7], linea[6])    
                    elif categoria == "motocicleta":
                        c.vehiculo_actual = clases.Motocicleta(linea[0], linea[1], categoria, \
                            linea[3], linea[4], linea[5], linea[7], linea[6])    
                    elif categoria == "troncomóvil":
                        c.vehiculo_actual = clases.Troncomovil(linea[0], linea[1], categoria, \
                            linea[3], linea[4], linea[5], linea[7], linea[6]) 
                    elif categoria == "bicicleta":
                        c.vehiculo_actual = clases.Bicicleta(linea[0], linea[1], categoria, \
                            linea[3], linea[4], linea[5], linea[7], linea[6])  

def ordenar(jugador, contrincantes):
    rivales = []
    for c in contrincantes:
        rivales.append(c)
    rivales.append(jugador)
    rivales.sort(key = lambda x:x.tiempo_acum)
    return rivales

def accidentar(prob, personas, jugador):
    x = uniform(0, 1)
    for persona in personas:
        prob = float(form.probabilidad_accidente(persona, persona.vehiculo_actual, \
            jugador.pista_actual))
        if x < prob:
            persona.vehiculo_actual.chasis_actual = 0

def verificar_descalificados(contrincantes, posiciones):
    descalificados = []
    for c in contrincantes:
        if c.vehiculo_actual.chasis_actual == 0:
            descalificados.append(c)
    for descalificado in descalificados:
        posiciones.remove(descalificado)
    return [descalificados, posiciones]

def nombre_valido(username):
    username = username.split(" ")
    for palabra in username:
        if not str.isalnum(palabra):
            return False
    return True

def nombre_repetido(jugador, nombre):
    with open(p.PATHS['VEHICULOS'], 'r', encoding="utf-8") as file:
        file.readline().strip().split(',')
        for linea in file:
            linea = linea.strip().split(',')
            if jugador.nombre == linea[1] and nombre == linea[0]:
                return True
    return False

def validar_input(opcion, i, n):
    opcion = str(opcion)
    while len(opcion) > 1 or len(opcion) == 0 or ord(str(opcion)) < 48+int(i) \
        or ord(str(opcion)) > 48+int(n):
        opcion = input("Seleccione una opción válida: ")
    return int(opcion)