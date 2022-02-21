# Archivo con todas las fórmulas
import parametros as p
import math

def calcular_hipotermia(pista, jugador):
    return min(0, pista.vuelta_actual * (jugador.contextura - pista.hielo))

def dif_control_vehiculo(vehiculo, jugador):
    if vehiculo.categoria == "motocicleta" or vehiculo.categoria == "bicicleta":
        if jugador.personalidad == "osado":
            return min(0, jugador.equilibrio - math.floor(p.PESO_MEDIO/vehiculo.peso))
        elif jugador.personalidad == "precavido":
            return min(0, jugador.equilibrio*p.EQUILIBRIO_PRECAVIDO - \
                math.floor(p.PESO_MEDIO/vehiculo.peso))
    return 0

def daño_recibido_cada_vuelta(vehiculo, pista):
    return int(max(0, int(pista.rocas - vehiculo.carroceria)))

def dinero_vuelta_x(pista):
    return int(pista.vuelta_actual * pista.dificultad)

def probabilidad_accidente(jugador, vehiculo, pista):
    if vehiculo.chasis > 0:
        return min(1, max(0, (calcular_velocidad_real(jugador, vehiculo, pista) - \
            calc_vel_rec(jugador, vehiculo, pista))/calc_vel_rec(jugador, vehiculo, pista)) \
                + math.floor((vehiculo.chasis - vehiculo.chasis_actual)/vehiculo.chasis))
    else:
        return 1

def tiempo_vuelta(jugador, vehiculo, pista, pits):
    if not pits:
        return int(math.ceil(pista.largo/calcular_velocidad_real(jugador, vehiculo, pista)))
    return int(math.ceil(pista.largo/calcular_velocidad_real(jugador, vehiculo, pista)) \
         + tiempo_pits(vehiculo))

def tiempo_pits(vehiculo):
    return int(p.TIEMPO_MINIMO_PITS + p.VELOCIDAD_PITS*(vehiculo.chasis - vehiculo.chasis_actual))

def calc_vel_rec(jugador, vehiculo, pista):
    if pista.tipo == 'pista suprema':
        if vehiculo.categoria == 'automóvil' or vehiculo.categoria == 'motocicleta':
            return (vehiculo.motor + (vehiculo.ruedas - \
                pista.hielo)*p.POND_EFECT['POND_EFECT_HIELO']\
                + (vehiculo.carroceria - pista.rocas)*p.POND_EFECT['POND_EFECT_ROCAS'] + \
                    (jugador.experiencia - pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
        else:
            return (vehiculo.zapatillas + (vehiculo.ruedas - \
                pista.hielo)*p.POND_EFECT['POND_EFECT_HIELO']\
                + (vehiculo.carroceria - pista.rocas)*p.POND_EFECT['POND_EFECT_ROCAS'] + \
                    (jugador.experiencia - pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
    elif pista.tipo == 'pista hielo':
        if vehiculo.categoria == 'automóvil' or vehiculo.categoria == 'motocicleta':
            return (vehiculo.motor + (vehiculo.ruedas - \
                pista.hielo)*p.POND_EFECT['POND_EFECT_HIELO']\
                + (jugador.experiencia - pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
        else:
            return (vehiculo.zapatillas + (vehiculo.ruedas - \
                pista.hielo)*p.POND_EFECT['POND_EFECT_HIELO']\
                + (jugador.experiencia - pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
    elif pista.tipo == 'pista rocosa':
        if vehiculo.categoria == 'automóvil' or vehiculo.categoria == 'motocicleta':
            return (vehiculo.motor + (vehiculo.carroceria - \
                pista.rocas)*p.POND_EFECT['POND_EFECT_ROCAS'] + (jugador.experiencia - \
                    pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
        else:
            return (vehiculo.zapatillas + (vehiculo.carroceria - \
                pista.rocas)*p.POND_EFECT['POND_EFECT_ROCAS'] + (jugador.experiencia - \
                    pista.dificultad)*p.POND_EFECT['POND_EFECT_DIFICULTAD'])
    
def calcular_velocidad_intencional(jugador, vehiculo, pista):
    if jugador.personalidad == 'osado':
        return p.EFECTO_OSADO * calc_vel_rec(jugador, vehiculo, pista)
    elif jugador.personalidad == 'precavido':
        return p.EFECTO_PRECAVIDO * calc_vel_rec(jugador, vehiculo, pista)

def calcular_velocidad_real(jugador, vehiculo, pista):
    return  max(p.VELOCIDAD_MINIMA, calcular_velocidad_intencional(jugador, vehiculo, pista)\
         + dif_control_vehiculo(vehiculo, jugador) + calcular_hipotermia(pista, jugador))

def dinero_ganador(pista):
    return int(pista.vueltas * (pista.dificultad + pista.hielo + pista.rocas))

def ventaja_con_ultimo_lugar(posiciones):
    n = int(len(posiciones))
    return posiciones[n-1].tiempo_acum - posiciones[0].tiempo_acum

def experiencia_recibida(jugador, pista, posiciones):
    if jugador.personalidad == "osado":
        return p.BONIFICACION_OSADO * (ventaja_con_ultimo_lugar(posiciones) + pista.dificultad)
    elif jugador.personalidad == "precavido":
        return p.BONIFICACION_PRECAVIDO * (ventaja_con_ultimo_lugar(posiciones) + pista.dificultad)