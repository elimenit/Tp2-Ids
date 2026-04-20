"""
Validacion del endpoint /partidos.
Recordar siempre el naveguador miente. 
"""
from datetime import datetime

def validar_fecha(fecha: str)-> bool:
    es_valida = False
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        es_valida = True
    except ValueError:
        es_valida = False
    return es_valida


def validar_offset_limit(limit: int, offset: int) -> bool:
    es_valido: bool = False

    if limit <= 10 and limit >= 0 and offset >= 0:
        es_valido = True
    
    return es_valido 

def validar_id_partido(id_partido: int) -> bool:
    """Valida el id de un partido
    Pre: necesita un id
    Post. verifica que un partido pueda tener id
    
    Args:
        id_partido (int):id del partido

    Returns:
        bool: si el id_partido es valido
    """
    es_valido = False
    if id_partido > 0:
        es_valido = True
    
    return es_valido

def validar_goles_local_visitante_positivos(gl: int, gv: int)-> bool:
    """Goles Positivos

    Args:
        gl (int): cantidad de goles del partido local
        gv (int): cantidad de goles del partido visitante

    Returns:
        bool: es valido
    """
    es_valido = False
    if gl > 0 and gv > 0:
        es_valido = True
    
    return es_valido