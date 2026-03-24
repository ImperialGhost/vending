from enums import tipoProducto


class Producto:
    def __init__(self,nombre: str, precio: float, cantidad: int, tipo: tipoProducto):
        self.nombre = nombre
        self.preco = precio
        self.cantidad = cantidad
        self.tipo = tipo