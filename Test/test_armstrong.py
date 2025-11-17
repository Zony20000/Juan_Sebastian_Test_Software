import pytest
import random
from App.armstrong import ArmStrong as ars

def test_armstrong_real():
    # Arrange (Preparación)
    entrada = 153
    resultado_esperado = "Has conseguido un numero de ArmStrong, narcisita."
    
    # Act (Acción)
    resultado_actual = ars(entrada)
    
    # Assert (Verificación)
    assert resultado_actual == resultado_esperado

def test_armstrong_fake():
    # Arrange (Preparación)
    entrada = 123
    resultado_esperado = "Solo conseguiste un numero mas."
    
    # Act (Acción)
    resultado_actual = ars(entrada)
    
    # Assert (Verificación)
    assert resultado_actual == resultado_esperado

def test_armstrong_zero():
    # Arrange (Preparación)
    entrada = 0
    resultado_esperado = "Numero diferente de Cero"
    
    # Act (Acción)
    resultado_actual = ars(entrada)
    
    # Assert (Verificación)
    assert resultado_actual == resultado_esperado

def test_armstrong_negative():
    # Arrange (Preparación)
    entrada = -153
    resultado_esperado = "Numero positivo necesario"
    
    # Act (Acción)
    resultado_actual = ars(entrada)
    
    # Assert (Verificación)
    assert resultado_actual == resultado_esperado

# Prueba Big Gang - Prueba de Estres si falla se encuentra algun nuevo punto a tener en cuenta
def test_armstrong_random():
    # Arrange (Preparación)
    entrada = random.randint(-2222222222222222222,2222222222222222222)
    
    # Act (Acción)
    resultado_actual = ars(entrada)
    
    # Assert (Verificación)
    assert resultado_actual == "Numero diferente de Cero" or resultado_actual == "Numero diferente de Cero" or resultado_actual == "Numero positivo necesario" or resultado_actual == "Has conseguido un numero de ArmStrong, narcisita." or resultado_actual == "Solo conseguiste un numero mas."
