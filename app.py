"""
Programa principal de la Aplicacion!!!
tiene que ser ejecutada con:
"flask run" o python3 app.py
Por defecto corre en el puerto 5000
"""
from flask import Flask
# DB
from database.db_init import iniciar_base_datos
# Routers
from routers.partidos import bp_partidos
from routers.usuarios import bp_usuarios
from routers.ranking import bp_ranking

app = Flask(__name__)

# Para la proxima sigue el ORM Aqui
iniciar_base_datos()
app.register_blueprint(bp_partidos)
app.register_blueprint(bp_usuarios)
app.register_blueprint(bp_ranking)

# Porfavor en el main no deberia haber nada usemos Blueprints para la modularizacion -> /routers
# AQUI ABAJO LAS CONFIGURACIONES
# :::
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)