# En la defensa del estudiantes se redacta que directamente le dio al estudiante la respuesta completa que de otra forma daria igual entonces gracias?
# No obstante se realiza un proceso de entendimiento por medio de comentarios para demostrar entendimiento
class Product:
    #Constructor de la clase con los atributos estandar del objeto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class ShoppingCart:
    #Constructor de la clase para un objeto que en este caso se consideraria el usuario con su carrito de compras
    def __init__(self):
        self.productos = []
        self.total = 0

    # Funcion para actualzar los datos dentro del objeto de carros de compra
    def add_item(self, producto, cantidad):
        if producto.stock >= cantidad:# verificamos que el usuario no realice compras imposibles
            self.productos.append((producto, cantidad)) # se agrega al final de la pila los datos del nuevo producto
            self.total += producto.precio * cantidad #actualizamos la variable total en base al valor del producto
            producto.stock -= cantidad # actualizar el stock del producto en base a los elementos comprados por el usuario
            return True
        return False
