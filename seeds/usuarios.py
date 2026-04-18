from schemas.usuario import UsuarioBase
from flask import Response
from utils.errores import error_response

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

def validacion_existencia_usuario(user_id: int, ids_list: list) -> tuple[bool, Response | None]:
    """
    Valida que el usuario exista en la DB. Si no cumple, devuelve una Response en el formato indicado en el swagger
    """
    if (user_id not in ids_list):
        return False, error_response(
            "Input error",
            "ERROR_NOT_FOUND",
            f"No se han encontrado coincidencias para el ID: {user_id}. Ingrese un numero entre {min(ids_list)} a {max(ids_list)}.",
            404
        )
    return True, None