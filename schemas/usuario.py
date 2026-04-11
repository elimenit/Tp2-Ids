class UsuarioBase():
    nombre: str
    email: str

class UsuarioResumen():
    id: int
    nombre: str

class Usuario(UsuarioBase):
    id: int