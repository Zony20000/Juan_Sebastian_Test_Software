#import random
# Obtener un numero aleatorio para saaber que hacer
#numero_aleatorio = random.randint(1, 4)

# mostrar numero
#print(numero_aleatorio)

#Code/Test2/venv/App/exercise_random.py 4 Este es el resultado obtenido en random

from functools import reduce

# ---------------- Explciacion de Uso ------------------------
# Reduce: Permite tomar valor por valor, con el fin de dar un orden estandar a los numeros u elementos dentro de un array

#Funcion de Suma con array

def plus(a:[]):
    return sum(a)

#Funcion de Resta con array

def minus(a:[]):
    return reduce(lambda c,b: c-b,a)

# Funcion de Multiplicacion con array

def times(a:[]):
    return reduce(lambda c,b: c*b,a)

# Funcion de Division con array

def divide_by(a:[]):
    try:
        return reduce(lambda c,b: c/b,a)
    except ZeroDivisionError:
        return "No se Divide por Cero"
    except Exception as e:
        return "La tumbaste, prueba revisar esto: ",e
