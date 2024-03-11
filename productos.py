class Producto:
    def __init__(self, codigo, descripcion, valorUnitario, stockDisponible):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valorUnitario = valorUnitario
        self.stockDisponible = stockDisponible
        self.siguiente = None
