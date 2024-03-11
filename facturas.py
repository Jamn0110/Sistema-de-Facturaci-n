class Factura:
    def __init__(self, numero, fecha, cliente, detalles, total):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.detalles = detalles
        self.total = total
        self.siguiente = None