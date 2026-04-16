"""
Inicializa la Base de datos y ejecuta las consultas al iiciar la aplicacion 
"""
from database.db import get_connection
import mysql.connector

from database.db import HOST, USER, PASSWORD, PORT, DBNAME

print(HOST, USER, PASSWORD, PORT, DBNAME)
def iniciar_base_datos():
    """ Inicializa la base de datos
    Pre: Necesita que el DBMS este corriendo y que solo se ejecute al iniciar la Aplicacion de flask.
    Post: Ejecuta consultas para inicializar la base de datos.
    """
    archivo = open(file="database/init_db.sql", mode="r")
    consultas_sql = archivo.read().split(";")
    archivo.close()

    conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
    cursor = conn.cursor()  # Session

    for query in consultas_sql:
        if query.strip():
            print(f"Se jecuta la query: {query}")
            cursor.execute(query)
            conn.commit()
            print("query ejecutada con exito!")

    cursor.close()
    conn.close()
