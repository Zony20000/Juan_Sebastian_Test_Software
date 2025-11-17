import pytest
from App.exercise_random import *

#Pruebas de Regresion

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

datos= [1,2,3,4,5,6,7,8,9,0]

def test_plus_fast(benchmark):

    benchmark(plus,datos)

def test_minux_fast(benchmark):

    benchmark(minus,datos)

def test_times_fast(benchmark):

    benchmark(times,datos)

def test_divide_fast(benchmark):

    benchmark(divide_by,datos)