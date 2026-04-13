class UsuarioBase():
    nombre: str
    email: str
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class UsuarioResumen():
    id: int
    nombre: str

class Usuario(UsuarioBase):
    def __init__(self, id, nombre, email):
        super().__init__(nombre, email)
        self.id = id
    