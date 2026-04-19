""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/partidos.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
"""
from database.db import get_connection

from schemas.partido import PartidoBase, Partido

def db_obtener_partidos(equipo=None, fecha=None, fase=None, limit=10, offset=0):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM partidos"
    filtros = []
    params = []

    if equipo:
        filtros.append("(equipo_local = %s OR equipo_visitante = %s)")
        params.extend([equipo, equipo])

    if fecha:
        filtros.append("fecha = %s")
        params.append(fecha)

    if fase:
        filtros.append("fase = %s")
        params.append(fase)

    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    query += " LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results

def db_obtener_partido(partido_id: int)-> Partido | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            p.id,
            p.equipo_local,
            p.equipo_visitante,
            p.fecha,
            f.nombre AS fase,
            r.goles_local,
            r.goles_visitante
        FROM partidos p
        JOIN fases f ON p.fase_id = f.id
        LEFT JOIN resultados r ON p.id = r.partido_id
        WHERE p.id = %s;
    """
    filtros = []
    params = [] 
    cursor.execute(query, (partido_id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return None

    return Partido(
        id= row["id"],
        equipo_local= row["equipo_local"],
        equipo_visitante= row["equipo_visitante"],
        fecha= row["fecha"].strftime("%Y-%m-%d") if row["fecha"] else "",
        fase= row["fase"],
        resultado= {
            "local": row["goles_local"],
            "visitante": row["goles_visitante"]
        } if row["goles_local"] is not None else {}
    )
    
def db_crear_partido(equipo_local: str, equipo_visitante: str, fecha: str, fase: str)-> int:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id FROM fases WHERE nombre = %s", (fase,))
    f = cursor.fetchone()

    insert_query = """
        INSERT INTO partidos (equipo_local, equipo_visitante, fecha, fase_id)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(insert_query, (equipo_local, equipo_visitante, fecha, f["id"]))
    conn.commit()

    partido_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return partido_id

def db_actualizar_partido(id: int, equipo_local: str, equipo_visitante: str, fecha: str, fase: str)-> None|int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM fases WHERE nombre = %s", (fase,))
    f = cursor.fetchone()
    if f is None:
        cursor.close()
        conn.close()
        return None
    query = """
        UPDATE partidos 
        SET equipo_local = %s, equipo_visitante = %s,
            fecha = %s, fase_id = %s
        WHERE id = %s
    """
    cursor.execute(query, (equipo_local, equipo_visitante, fecha, f[0], id))
    cursor.close()
    conn.commit()
    conn.close()
    return id

def db_actualizar_parcialmente_partido():
    conn = get_conexion()
    pass

def db_eliminar_partido(id: int)-> bool:
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM partidos WHERE id = %s"
    cursor.execute(query, (id, ))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def db_actualizar_resultado(id: int, goles_local: int, goles_visitante: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # 1. verificar partido existe
    cursor.execute("SELECT id FROM partidos WHERE id = %s", (id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return False

    # 2. verificar si existe resultado
    cursor.execute(
        "SELECT 1 FROM resultados WHERE partido_id = %s",
        (id,)
    )
    existe = cursor.fetchone()

    if existe:
        cursor.execute(
            """
            UPDATE resultados
            SET goles_local = %s, goles_visitante = %s
            WHERE partido_id = %s
            """,
            (goles_local, goles_visitante, id)
        )
    else:
        cursor.execute(
            """
            INSERT INTO resultados (partido_id, goles_local, goles_visitante)
            VALUES (%s, %s, %s)
            """,
            (id, goles_local, goles_visitante)
        )

    conn.commit()
    cursor.close()
    conn.close()

    return True

def db_obtener_prediccion():
    conn = get_conexion()
    pass