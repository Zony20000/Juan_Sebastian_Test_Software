#import random
# Obtener un numero aleatorio para saaber que hacer
#numero_aleatorio = random.randint(1, 4)

# mostrar numero
#print(numero_aleatorio)

#Code/Test2/venv/App/exercise_random.py 4 Este es el resultado obtenido en random

from functools import reduce

def plus(a:[]):
    return sum(a)

def minus(a:[]):
    return reduce(lambda c,b: c-b,a)

def times(a:[]):
    return reduce(lambda c,b: c*b,a)

def divide_by(a:[]):
    try:
        return reduce(lambda c,b: c/b,a)
    except ZeroDivisionError:
        return "No se Divide por Cero"
    except Exception as e:
        return "La tumbaste, prueba revisar esto: ",e
