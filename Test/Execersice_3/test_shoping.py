from App.Execersice_3.Shopping import *
import pytest

def test_complete_purchase_system_flow():
    mouse = Product("Mouse", 50, 20)
    
    cart = ShoppingCart()
    
    assert cart.add_item(mouse, 2) == True
    
    # Verifica que el total sea correcto
    assert cart.total == 100
    
    # Verifica que el stock de los productos se actualice correctamente
    
    assert mouse.stock == 18

def test_sin_precios():
    
    excuse = Product("Excusas",0,10)#Solo por prueba pero mejor conseguir uno infinitos

    cart =ShoppingCart()
    #Compramos todas la excusas ;)
    assert cart.add_item(excuse,10) == True

    #Cuanto costo excusarse?
    assert cart.total == 0

    #Ahora nos acabamos razones para esto eje
    assert excuse.stock == 0

def test_compra_negativo():
    # En esta caso como es prueba y no solucion. 
    # -----------Report-------------
    # Reporto que es necesario manejar los valores negativos.
    # ------------------------------
    
    excuse = Product("Excusas",0,-1)#Solo por prueba pero mejor conseguir uno infinitos

    cart =ShoppingCart()
    #Compramos todas la excusas ;)
    assert cart.add_item(excuse,1) == False

    #Cuanto costo excusarse?
    assert cart.total == 0

    #Ahora nos acabamos razones para esto eje
    assert excuse.stock == -1
