# En la defensa del estudiantes se redacta que directamente le dio al estudiante la respuesta completa que de otra forma daria igual entonces gracias?
class Product:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.productos = []
        self.total = 0

    def add_item(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
            self.total += producto.precio * cantidad
            producto.stock -= cantidad
            return True
        return False
