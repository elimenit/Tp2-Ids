from utils.errores import error_response
from typing import Any
from flask import Response 

"""
Este archivo concentra la lógica de paginación para cualquier endpoint
"""
def calcular_offset(limit: int, offset: int, total_resultados: int) -> dict:
    """
    Calcula el offset en el cual se tiene que estar parado, devolviendo
    un diccionario que contiene los 4 casos posibles
    """ 
    resto = total_resultados % limit
    last = total_resultados - resto
    if resto == 0:
        last = total_resultados - limit
    return {
        "first": 0,
        "prev": offset - limit,
        "next": offset + limit,
        "last": last
    }
def crear_response_paginacion(limit: int, offset: int, total_resultados: int, base: str) -> tuple[bool, Any]:
    """ 
    Crea el diccionario que especificado en el swagger
    ### Recibe:
    - Limite de registros por pagina
    - Offset
    - El total de los resultados
    - La URL base
    ### Devuelve:
    - Un diccionario con la estructura del paginado
    """
    actual_offset = calcular_offset(limit, offset, total_resultados)
    if offset < limit:
        actual_offset["prev"] = 0
    if offset >= total_resultados:
        actual_offset["next"] = actual_offset["last"]
    response = {
            "_first": {
            "href": f"{base}?_offset={actual_offset['first']}&_limit={limit}"
            },
            "_prev": {
            "href": f"{base}?_offset={actual_offset['prev']}&_limit={limit}"
            },
            "_next": {
            "href": f"{base}?_offset={actual_offset['next']}&_limit={limit}"
            },
            "_last": {
            "href": f"{base}?_offset={actual_offset['last']}&_limit={limit}"
            }
        }
    return True, response

def validar_offset(offset: int, total_resultados: int) -> tuple[bool, Response | None]:
    """
    Valida que el offset ingresado sea menor al total de resultados. Si no cumple, devuelve 
    un valor booleano False y una Response con el formato del swagger
    """
    if offset >= total_resultados:
        return False, error_response(
            "Error de input",
            "INVALID_OFFSET",
            f"Ingrese un offset menor a {total_resultados}",
            400 
        )
    return True, None