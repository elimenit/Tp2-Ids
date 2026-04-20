"""
Implementacion del Endpoint de ranking:
GET /ranking
# FINAL 
PAGINACION (limit  - offset)
"""
from flask import Blueprint, jsonify, request
from database.ranking import obtener_ranking_db, contar_rankings
from utils.errores import error_response
from utils.paginacion import crear_response_paginacion, validar_offset

bp_ranking = Blueprint("ranking", __name__, url_prefix="/ranking")

@bp_ranking.route("/", methods=["GET"])
def obtener_ranking():
    """Obtener Ranking
    Pre: Debe haber partidos juguados
    Post: Devuelve el ranking 
    """
    limit = request.args.get("_limit", default=10, type=int)
    offset = request.args.get("_offset", default=0, type=int)

    base = request.base_url
    try:
        rankings_data = obtener_ranking_db(limit, offset)
    except Exception as e:
        return error_response(
            "Error del servidor",
            "INTERNAL_SERVER_ERROR",
            f"Ha ocurrido un error durante la obtencion de rankings: {e}",
            500
        )

    cant_rankings = contar_rankings()
    offset_ok, offset_response = validar_offset(offset, cant_rankings)
    if not offset_ok:
        return offset_response
    
    response_pages = crear_response_paginacion(limit, offset, cant_rankings, base)
    
    list_rankings = [{'puntos': puntos, 'id': id} for puntos, id in rankings_data]

    response = {
        "metadata": {
            "cant_rankings": cant_rankings
        },
        "ranking": list_rankings,
        "_links": response_pages
    }
    return jsonify(response), 200