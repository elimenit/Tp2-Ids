""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/usuarios.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
Opcional:
    Por favor las contraseñas se guardan hasheadas ;).
"""
from database.db import get_connection
from schemas.usuario import UsuarioBase, Usuario

def db_obtener_usuarios(_limit: int, _offset: int) -> list[tuple[int, str, str]]:
    """
    Devuelve una lista con los registros de la tabla usuarios ordenados por ID
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT id, nombre, email
                FROM usuarios
                ORDER BY id
                LIMIT %s OFFSET %s;
            """
            cursor.execute(query, (_limit, _offset))
            results = cursor.fetchall()
    return results

def db_obtener_usuario(user_id) -> Usuario|None:
    """Obtiene un usuario o None
    Pre: Necesita un id
    Post: Devuelve un Usuario o None
    Args:
        user_id (_type_): _description_
    """
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return Usuario(id=user[0], nombre=user[1], email=user[2])

def db_crear_usuario(user_recv: UsuarioBase)-> Usuario:
    """Creacion de un Usuario
    Contrato con los Routers:
    Pre: Recibe un UsuarioBase Verificado y valido .
    Post: Crea un usuario y lo devuelve.
    Args:
        user_recv (UsuarioBase): usuario con los datos a crear.
    Returns:
        Usuario: usuario que esta almacenado en la Base de Datos. 
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios(nombre, email) VALUES (%s, %s);", (user_recv.nombre, user_recv.email))
    cursor.execute("SELECT LAST_INSERT_ID()") # Propio de MySQL
    new_id = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (new_id, ))
    user = cursor.fetchone()
    print(user)
    print(type[new_id])
    print(new_id)
    conn.commit()
    cursor.close()
    conn.close()
    return Usuario(id=user[0], nombre=user[1], email=user[2])


def db_actualizar_usuario(user: Usuario) -> Usuario:
    """actualiza un Usuario.
    Pre: Necesita los campos de un Usuario.
    Post: Actualiza y devuelve el Usuario actualizado.
    Args:
        user (Usuario): Usuario a actualizar.

    Returns:
        Usuario: Usuario actualizado.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"
    cursor.execute(query, (user.nombre, user.email, user.id))
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user.id,))
    user = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()
    return Usuario(id=user[0], nombre=user[1], email=user[2])
    

def db_eliminar_usuario(id_user: int) -> Usuario:
    """elimina un usuario por su id.
    Pre: EL id debe existir.
    Post: elimina y devuelve el usuario eliminado.

    Args:
        id_user (int): id del usuario eliminado.

    Returns:
        _type_: _description_
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_user,))
    user = cursor.fetchone()
    query = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(query, (id_user,))
    conn.commit()
    cursor.close()
    conn.close()
    return Usuario(id=user[0], nombre=user[1], email=user[2])



