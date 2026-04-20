class UsuarioBase():
    nombre: str
    email: str
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email
        }

class UsuarioResumen():
    id: int
    nombre: str

class Usuario(UsuarioBase):
    def __init__(self, id, nombre, email):
        super().__init__(nombre, email)
        self.id = id

    def to_dict(self):
        data = super().to_dict()
        data["id"] = self.id
        return data    
