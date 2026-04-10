# Funcionalidades del directorio database
"""
Se muestra como esta implementada la base de datos nos debe de mostrar una interfaz simple y amigable.
"""
## /database/conexion.py
"""
Muestra como esta configurado la conexion con el DBMS(DATABASE MANAGE SYSTEM) mysql para
las querys o consultas a las base de datos
"""

#### REQUERIDO
Como carguar una variable de entorno(PASSWORD)
´´´
from dotenv import load_dotenv
import os
load_dotenv()
password = os.getenv("PASSWORD") # en el archivo .env PASSWORD="clave secreta"
print(password)
´´´
