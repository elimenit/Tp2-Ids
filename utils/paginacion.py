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
def crear_response_paginacion(limit: int, offset: int, total_resultados: int, base: str) -> dict:
    """
    Crea la response. En caso de que no haya registros suficientes para mostrar una
    página en concreto, lo especifica
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
    return response