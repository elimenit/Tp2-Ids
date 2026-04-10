import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv() # carga las variables de entorno del .env <- Borra despues

HOST=os.getenv("HOST_DB_MYSQL")
USER=os.getenv("USER_DB_MYSQL")
PASSWORD=os.getenv("PASSWORD_DB_MYSL")
DATABASE =os.getenv("NAME_DB_MYSQL")
PORT=os.getenv("PORT_DB_MYSQL")

def get_conexion():
    """ Conecion con la Base de datos
    Pre: Necesita que el DBMS (DATABASE MANAGE SISTEM) este activo 
        y correctamente configurado con user y password configurados.
    Post: devuelva un cursor que nos permite ejecutar consultas a nuestro DBMS.
    Returns:
        Session: devuelve una session o un cursor para ejecutar las consultas.
    """
    return mysql.connector.connect(
        host="localhost", user=USER, 
        dbname=DATABASE, port=PORT
    )
