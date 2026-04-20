""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/ranking.py
## La implementacion es libre de realizarse mientras se cumpla el contrato

"""
from database.db import get_connection

def obtener_ranking_db(limit: int, offset: int) -> list[tuple[int, int]]:
    """
    Obtiene el ranking ordenado descendientemente en base a sus puntos. Recibe parámetros LIMIT y OFFSET.
    """
    query = """
        SELECT puntos, usuario_id FROM ranking
        ORDER BY puntos DESC
        LIMIT %s
        OFFSET %s
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit, offset))
            return cur.fetchall()

def contar_rankings() -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM ranking")
            resultado = cur.fetchone()
            return int(resultado[0]) if resultado else 0