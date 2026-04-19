""" 
Validacion sin usar la conexion a la Base de Datos
Recordar el Naveguador siempre miente, asi que validemos que no nos mienta
"""
from schemas.usuario import UsuarioBase, Usuario

def validacion_offset_limit(limit: int, offset: int)-> bool:
    """Valida que el usuario no pida demas

    Args:
        offset (int): desde donde empieza
        limit (int): cuantos resultados va ha obtener

    Returns:
        bool: si los parametros ingresados son validos
    """
    es_valido: bool = False
    if limit < 10 and limit > 0 and offset >= 0:
        es_valido = True

    return es_valido

def validacion_creacion_usuario(user: UsuarioBase) -> bool:
    """Verificacion de un usuario en su creacion
    Pre: Debe recibir la informacion de un usuario a crear
    Post: Devuelve un booleano que le indica que el usuario es valido o no
    Args:
        chek_user (UsuarioBase): informacion recibida de un usuario
    Returns:
        bool: Validacion si es el chek_user es valido para ingresarlo a la BD
    """
    if not user.nombre or not user.nombre.strip():
        return False
    if not user.email or "@" not in user.email:
        return False
    return True

def validacion_campos_usuario(user: Usuario) -> bool:
    """Valida los campos de un Usuario.
    Pre: Necesita el Usuario a validar.
    Post: devuelve si es valido.

    Args:
        user (Usuario): Usuario a validar

    Returns:
        bool: Si el usuario es valido.
    """
    es_valido: bool = False # Naveguador siempre miente
    
    if validacion_id_usuario(user.id):
        if user.nombre is not None:
            if user.nombre.strip() != "":
                if user.email is not None:
                    if "@" in user.email:
                        es_valido = True
            
    return es_valido

def validacion_id_usuario(id: int) -> bool:
    """Valida un id valido
    Pre: Necesita el id de un usario
    Post: Devuelve un booleano
    Args:
        id (int): id de un usuario

    Returns:
        bool: si es valido el id
    """
    id_valido: bool = False
    
    if id > 0:
        id_valido = True

    return id_valido