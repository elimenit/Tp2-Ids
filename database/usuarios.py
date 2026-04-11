""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/usuarios.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
Opcional:
    Por favor las contraseñas se guardan hasheadas ;).
"""
from database.db import get_connection

def obtener_usuarios(limit: int = 10, offset: int = 10):
    conn = get_conexion()
    pass

def obtener_usuario():
    conn = get_conexion()
    pass

def crear_usuario():
    conn = get_conexion()
    pass

def actualizar_usuario():
    conn = get_conexion()
    pass

def actualizar_parcialmente_usuario():
    conn = get_conexion()
    pass

def eliminar_usuario():
    query = ""
    conn = get_conexion()
    conn.execute(query)
    conn.close()
    pass


