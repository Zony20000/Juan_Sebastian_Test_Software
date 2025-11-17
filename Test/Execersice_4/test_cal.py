import pytest
import random
from App.Execersice_4.exercise_random import *

#Pruebas de Regresion

# En este caso no usamos un valor random sino se genera una funcion por cada caso de prueba

def test_plus_positive():
    numbers = [1,2]

    resultado_esperado = 3
    resultado_actual = plus(numbers)

    assert resultado_actual == resultado_esperado

def test_plus_negativa():
    numbers = [1,-2]
    
    resultado_esperado = -1
    resultado_actual = plus(numbers)

    assert resultado_actual == resultado_esperado

def test_plus_zero():
    numbers = [0,0]
    
    resultado_esperado = 0
    resultado_actual = plus(numbers)

    assert resultado_actual == resultado_esperado

def test_minus_positive():
    numbers = [2,1]
    
    resultado_esperado = 1
    resultado_actual = minus(numbers)

    assert resultado_actual == resultado_esperado

def test_minus_negative():
    numbers = [-2,-1]

    resultado_esperado = -1
    resultado_actual = minus(numbers)

    assert resultado_actual == resultado_esperado

def test_minus_zero():
    numbers = [0,0]

    resultado_esperado = 0
    resultado_actual = minus(numbers)

    assert resultado_actual == resultado_esperado
    
def test_minus_zero():
    numbers = [0,0]

    resultado_esperado = 0
    resultado_actual = minus(numbers)

    assert resultado_actual == resultado_esperado

def test_times_positive():
    numbers = [4,4]

    resultado_esperado = 16
    resultado_actual = times(numbers)

    assert resultado_actual == resultado_esperado

def test_times_negative():
    numbers = [-4,-4]

    resultado_esperado = 16
    resultado_actual = times(numbers)

    assert resultado_actual == resultado_esperado

def test_times_zero():
    numbers = [1,0]

    resultado_esperado = 0
    resultado_actual = times(numbers)

    assert resultado_actual == resultado_esperado

def test_divide_by_positive():
    numbers = [4,4]

    resultado_esperado = 1
    resultado_actual = divide_by(numbers)

    assert resultado_actual == resultado_esperado

def test_divide_by_negative():
    numbers = [-4,-4]

    resultado_esperado = 1
    resultado_actual = divide_by(numbers)

    assert resultado_actual == resultado_esperado

def test_divide_by_zero():
    numbers = [1,0]

    resultado_esperado = "No se Divide por Cero"
    resultado_actual = divide_by(numbers)

    assert resultado_actual == resultado_esperado

# Pruebas de Rendimiento con benchmark
# Para usar benchmark debe usar pip install pytest-benchmark

# En este caso volvemos a establecer valores para probar y con benchmark lo repetimos varias veces y devuelve el tiempo que le toma realizar la prueba

datos= []
# esto es un aditamento para romper las funciones
for i in range(11):
    datos.append(random.randint(-2222222222222222222,2222222222222222222))

def test_plus_fast(benchmark):

    benchmark(plus,datos)

def test_minux_fast(benchmark):

    benchmark(minus,datos)

def test_times_fast(benchmark):

    benchmark(times,datos)

def test_divide_fast(benchmark):

    benchmark(divide_by,datos)