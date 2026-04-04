"""
Programa principal de la Aplicacion!!!
tiene que ser ejecutada con:
"flask run" 
"""
from flask import Flask

app = Flask(__name__)

# Porfavor en el main no deberia haber nada usemos Blueprints para la modularizacion -> /routers
