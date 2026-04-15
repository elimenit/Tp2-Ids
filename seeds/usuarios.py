from schemas.usuario import UsuarioBase

def validacion_creacion_usuario(chek_user: UsuarioBase) -> bool:
    """Verificacion de un usuario en su creacion
    Pre: Debe recibir la informacion de un usuario a crear
    Post: Devuelve un booleano que le indica que el usuario es valido o no
    Args:
        chek_user (UsuarioBase): informacion recibida de un usuario
    Returns:
        bool: Validacion si es el chek_user es valido para ingresarlo a la BD
    """
    es_valido: bool = True
    if chek_user.email is None:
        es_valido = False
        #raise Exception("Usuario con email invalido!")
    if chek_user.nombre is None:
        es_valido = False
        #raise Exception("Usuario con nombre invalido")
    
    return es_valido