"""
Programa principal de la Aplicacion!!!
tiene que ser ejecutada con:
"flask run" o python3 app.py
Por defecto corre en el puerto 5000
"""
from flask import Flask

app = Flask(__name__)

# Porfavor en el main no deberia haber nada usemos Blueprints para la modularizacion -> /routers
# AQUI ABAJO LAS CONFIGURACIONES
# :::