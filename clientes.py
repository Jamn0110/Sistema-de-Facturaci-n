class Cliente:
    def __init__(self, cedula, nombre, direccion, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.siguiente = None