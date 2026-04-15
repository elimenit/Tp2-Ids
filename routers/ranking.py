"""
Implementacion del Endpoint de ranking:
GET /ranking
# FINAL 
PAGINACION (limit  - offset)
"""
from flask import Blueprint

bp_ranking = Blueprint("ranking", __name__, url_prefix="/ranking")

@bp_ranking.route("/", methods=["GET"])
def obtener_ranking():
    """Obtener Ranking
    Pre: Debe haber partidos juguados
    Post: Devuelve el ranking 
    """
    pass