from flask import Response
from utils.errores import error_response

def verificar_campos_obligatorios(data: dict, campos_obligatorios: list) -> tuple[bool, Response | None]:
    """
    Esta función tranquilamente podria ser un helper cualquiera, sirve para cualquier apartado

    ### Recibe:
    - Diccionario
    - Lista de campos obligatorios
    ### Devuelve:
    - Valor booleano indicando éxito de la operación
    - Response en caso de falla
    """
    for campo in campos_obligatorios:
        if campo not in data or data[campo] is None or data[campo] == "":
            return False, error_response(
                "Error del usuario",
                "INPUT_ERROR",
                f"No se han detectado campos obligatorios -> Campos obligatorios: {campos_obligatorios}",
                400
            )
    return True, None