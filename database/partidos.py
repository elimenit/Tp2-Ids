""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/partidos.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
"""
from database.db import get_connection 
from datetime import date

def obtener_partido():
    conn = get_conexion()
    pass

def obtener_ids_partido(eq_local: str, eq_visitante: str, fase: str) -> dict[str, int]:
    """
    ### Recibe:
    - Equipo local
    - Equipo visitante
    - Fase
    ### Devuelve:
    - Un diccionario con las respectivas IDs
    """
    query = """
        SELECT 
            (SELECT id FROM equipos WHERE nombre = %s) AS id_local,
            (SELECT id FROM equipos WHERE nombre = %s) AS id_visitante,
            (SELECT id FROM fases WHERE nombre = %s) AS id_fase
    """
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute(query, (eq_local, eq_visitante, fase))
            return cur.fetchone()

def crear_partido_db(id_local: int, id_visitante: int, fecha: date, id_fase: int) -> None:
    """
    ### Recibe:
    - ID Equipo local
    - ID Equipo visitante
    - Fecha
    - ID Fase
    Y crea un registro en la tabla "partidos"
    """
    query = """
        INSERT INTO partidos (equipo_local_id, equipo_visitante_id, fecha, fase_id)
        VALUES (%s, %s, %s, %s)
    """
    with get_connection() as conn:
        with conn.cursor() as cur: 
            cur.execute(query, (id_local, id_visitante, fecha, id_fase))
        conn.commit()

def actualizar_partido():
    conn = get_conexion()
    pass

def actualizar_parcialmente_partido():
    conn = get_conexion()
    pass

def eliminar_partido():
    conn = get_conexion()
    pass

def obtener_partidos(limit: int=10, offset: int=10):
    conn = get_conexion()
    pass

def obtener_prediccion():
    conn = get_conexion()
    pass