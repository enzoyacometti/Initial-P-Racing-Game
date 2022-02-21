# Valores máximos y mínimos de las partes y el peso de los vehículos
import funciones as func
import random

AUTOMOVIL = {
    'CHASIS': {
        'MIN': 50,
        'MAX': 80
    },
    'CARROCERIA': {
        'MIN': 30,
        'MAX': 55
    },
    'RUEDAS': {
        'MIN': 70,
        'MAX': 80
    },
    'MOTOR': {
        'MIN': 90,
        'MAX': 95
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 90,
        'MAX': 150
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': 40,
        'MAX': 60
    },
    'CARROCERIA': {
        'MIN': 40,
        'MAX': 60
    },
    'RUEDAS': {
        'MIN': 50,
        'MAX': 75
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 30,
        'MAX': 50
    },
    'PESO': {
        'MIN': 70,
        'MAX': 90
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 40,
        'MAX': 50
    },
    'CARROCERIA': {
        'MIN': 40,
        'MAX': 50
    },
    'RUEDAS': {
        'MIN': 50,
        'MAX': 70
    },
    'MOTOR': {
        'MIN': 80,
        'MAX': 90
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': 50,
        'MAX': 70
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 30,
        'MAX': 40
    },
    'CARROCERIA': {
        'MIN': 35,
        'MAX': 45
    },
    'RUEDAS': {
        'MIN': 40,
        'MAX': 55
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': 30,
        'MAX': 50
    },
    'PESO': {
        'MIN': 10,
        'MAX': 20
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 300,
        'EFECTO': 2
    },
    'CARROCERIA': {
        'COSTO': 400,
        'EFECTO': 2
    },
    'RUEDAS': {
        'COSTO': 450,
        'EFECTO': 1.5
    },
    'MOTOR': {
        'COSTO': 380,
        'EFECTO': 2
    },
    'ZAPATILLAS': {
        'COSTO': 150,
        'EFECTO': 5
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': 'precavido'
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': random.choice(['precavido', 'osado'])
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': 'osado'
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 1.3
EFECTO_PRECAVIDO = 1.05

# Dificultad de control del vehículo
PESO_MEDIO = 1400
EQUILIBRIO_PRECAVIDO = 2

# Tiempo pits
TIEMPO_MINIMO_PITS = 30
VELOCIDAD_PITS = 20

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 1.1
BONIFICACION_OSADO = 1.2


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehículos.csv",
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None



###############################
## Parámetros creados por mi ##
###############################

NUMERO_CONTRINCANTES = 4
DINERO_INICIAL = 1000

POND_EFECT = {
    'POND_EFECT_HIELO': 0.01,
    'POND_EFECT_ROCAS': 0.01,
    'POND_EFECT_DIFICULTAD': 0.0001
}

PRECIOS = {
    'AUTOMOVIL': 1300,
    'TRONCOMOVIL': 900,
    'MOTOCICLETA': 700,
    'BICICLETA': 450
}