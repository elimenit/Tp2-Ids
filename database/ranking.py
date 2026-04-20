""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/ranking.py
## La implementacion es libre de realizarse mientras se cumpla el contrato

"""

from database.db import get_connection

def db_obtener_ranking(limit: int = 10, offset: int=0):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT u.id, u.nombre, r.puntos
        FROM ranking r
        JOIN usuarios u ON u.id = r.usuario_id
        ORDER BY r.puntos DESC
        LIMIT %s OFFSET %s;
    """

    cursor.execute(query, (limit, offset))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()
    return resultados