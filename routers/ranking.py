"""
Implementacion del Endpoint de ranking:
GET /ranking
# FINAL 
PAGINACION (limit  - offset)
"""
from flask import Blueprint, request

from database.db import get_connection
from database.ranking import db_obtener_ranking

from seeds.partidos import validar_offset_limit
from utils.errores import error_response

bp_ranking = Blueprint("ranking", __name__, url_prefix="/ranking")

@bp_ranking.route("/", methods=["GET"])
def obtener_ranking():
    """Obtener Ranking
    Pre: Debe haber partidos juguados
    Post: Devuelve el ranking 
    """
    limit = request.args.get("_limit", 10, type=int)
    offset = request.args.get("_offset", 0, type=int)
    if not validar_offset_limit(limit, offset):
        return error_response(
            code="400",
            message="Limit u offset no validos",
            level="MEDIO",
            description="Limit u Offset numeros muy grandes",
            status_code=400
        )
    return db_obtener_ranking(limit=limit, offset=offset)