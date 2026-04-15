""" Contrato de la API con SWAGGER
Implementacion de las consultas SQL para cumplir el contrato 
Pertenecen a /routers/ranking.py
## La implementacion es libre de realizarse mientras se cumpla el contrato

"""
from database.DB import get_connection
from flask import Blueprint

bp_ranking = Blueprint("ranking", __name__, url_prefix="/ranking")

@bp_ranking.route("/", methods=["GET"])
def obtener_ranking():
    """ Obtiene el ranking
    """
    pass
