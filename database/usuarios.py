""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/usuarios.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
Opcional:
    Por favor las contraseñas se guardan hasheadas ;).
"""
from database.db import get_connection
from schemas.usuario import UsuarioBase, Usuario

def db_obtener_usuarios() -> list[tuple[int, str, str]]:
    """
    Devuelve una lista con todos los registros de la tabla usuarios ordeandos por ID
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            query = "SELECT id, nombre, email FROM usuarios ORDER BY id;"
            cur.execute(query)
            results = cur.fetchall()
    return results

def db_crear_usuario(user_recv: UsuarioBase)-> Usuario:
    """Creacion de un Usuario
    Contrato con los Routers:
    Pre: recibe un UsuarioBase Verificado y valido .
    Post: devuelve un Usuario.
    Args:
        user_recv (UsuarioBase): usuario con los datos a crear.
    Returns:
        Usuario: usuario que esta almacenado en la Base de Datos. 
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO usuarios(nombre, email) VALUES ('{user_recv.nombre}', '{user_recv.email}');")
    cursor.execute(f"SELECT * FROM usuarios WHERE nombre='{user_recv.nombre}' AND email='{user_recv.email}';")
    user = cursor.fetchone()
    conn.commit()
    cursor.close()
    return Usuario(id=user[0], nombre=user[1], email=user[2])


def db_actualizar_usuario():
    conn = get_conexion()
    pass

def db_actualizar_parcialmente_usuario():
    conn = get_conexion()
    pass

def db_eliminar_usuario():
    query = ""
    conn = get_conexion()
    conn.execute(query)
    conn.close()
    pass


