class DetalleFactura:
    def __init__(self, producto, cantidad, precio, subtotal):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal
        self.siguiente = None