""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/partidos.py
## La implementacion es libre de realizarse mientras se cumpla el contrato
"""
from database.db import get_conexion

def obtener_partido():
    conn = get_conexion()
    pass

def crear_partido():
    conn = get_conexion()
    pass

def actualizar_partido():
    conn = get_conexion()
    pass

def actualizar_parcialmente_partido():
    conn = get_conexion()
    pass

def eliminar_partido(id_partido: int):
    conn = get_conexion()
    cursor = conn.cursor(dictionary=True)

    # Primero verifico si el partido existe antes de borrarlo
    cursor.execute("SELECT * FROM partidos WHERE id = %s", (id_partido,))
    partido = cursor.fetchone()

    if not partido:
        cursor.close()
        conn.close()
        return None 

    # Si existe, lo eliminamos
    cursor.execute("DELETE FROM partidos WHERE id = %s", (id_partido,))
    conn.commit()  # IMPORTANTE — confirma el cambio en la base de datos

    cursor.close()
    conn.close()
    return partido  

def obtener_partidos(limit: int=10, offset: int=10):
    conn = get_conexion()
    pass

def obtener_prediccion():
    conn = get_conexion()
    pass