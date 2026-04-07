# Funcionalidades del directorio database
"""
Se muestra como esta implementada la base de datos nos debe de mostrar una interfaz simple y amigable.
"""
## /database/db.py
"""
Nos muestra como esta echa por dentro la el Objeto DataBase y nos muestra operaciones
que podemos hacer con la base de datos 
"""

#### Opcional
Como carguar una variable de entorno(PASSWORD)
´´´
from dotenv import load_dotenv
import os
load_dotenv()
password = os.getenv("PASSWORD") # en el archivo .env PASSWORD="clave secreta"
print(password)
´´´
