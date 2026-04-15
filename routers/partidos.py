"""
Endpoint de partidos:
GET /partidos
POST /partidos

# por Id
GET /partidos/<id>"""

from database.db import get_connection

def obtener_partido(id_partido: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM partidos WHERE id = %s"
    cursor.execute(query, (id_partido,))

    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    return resultado
"""DElETE /partidos/<id>

# Resultados
PUT /partidos/id/resultado

# Opcionales
PUT /partidos/id
PATCH /partidos/id
# Final 
Paginacion a cada uno de los endpoints(Offset-limit)
Hasta cuanta informacion deberia enviar por request
"""
from flask import Blueprint, request, jsonify
from schemas.partido import (
    Partido, ResultadoPartido, PrediccionPartido
)

bp_partidos = Blueprint('partidos', __name__, url_prefix='/') 

@bp_partidos.route("/", methods=["GET"])
def listar():
    """Lista todos los Partidos
    Pre: Recibe todos los filtros para encontrar lo partidos que matcheen
    Post: devuelve partidos que cumplen los filtros

    Args:
        equipo (str): Nombre del equipo
        fecha (str): Una fecha con formato: AAAA-MM-DD
        fase (str): EN que fase de la copa se encuentra
        _limit (int): paginacion # Pueden editarlo si desean
        _offset (int): paginacion

    Returns:
        dict: devuelve una lista de partidos 
    """
    equipo = request.args.get("equipo", "")
    fecha = request.args.get("fecha", "")
    fase = request.args.get("fase", "")
    limit = request.args.get("_limit", 10, type=int)
    offset = request.args.get("_offset", 10, type=int)
    return jsonify({"hola": "mundo"})

@bp_partidos.route("/", methods=["POST"])
def crear():
    """ Creacion de un Partido
    Pre: Recibe en el Body la informacion de un partido
    Post: Devuelve el partido creado

    Returns:
        _type_: devuelve el equipo creado
    """
    return {} 

@bp_partidos.route("/<int:id>", methods=["GET"])
def obtener(id: int):
    """Obtiene un Partido
    Pre: recibe un id de un partido existente
    Post: devuelve el partido correspondiente
    
    Args:
        id (int): id del partido

    Returns:
        dict: El Objeto Partido
    """
    return Partido

@bp_partidos.route("/<int:id>", methods=["PUT"])
def actualizar(id: int):
    """Actualiza el partido

    Args:
        id (int): id del partido a actualizar

    Returns:
        Partido: el partido actualizado
    """
    pass

@bp_partidos.route("/<int:id>", methods=["PATCH"])
def actualizar_parcialmente(id: int):
    """Actualiza un partido parcialmente
    Pre: la informacion de los campos a modificar deben ser obtenidas del body
    Post: Actualizar parcialmente el campo del partido que no es None
    Args:
        id (int): id del partido

    Returns:
        Partido: partido actualizado
    """
    return Partido

@bp_partidos.route("/<int:id>", methods=["DELETE"])
def eliminar(id: int):
    """Elimina un partido
    Pre: Necesita el id de un partido existente
    Post: Elimina el prtido de la base de datos
    Args:
        id (int): identificador unico del partido

    Returns:
        Partido: partido eliminado
    """
    return Partido
    
@bp_partidos.route("/<int:id>/resultado", methods=["PUT"])
def mostrar_resultado(id: int):
    """Resultado de un partido
    Pre: necesita el id de un partido
    Post: devuelve el resultado de un partido
    Args:
        id (int): Id del partido

    Returns:
        ResultadoPartido: modelo de como resulto un partido
    """
    pass

@bp_partidos.route("/<int:id>/prediccion", methods=["POST"])
def predecir(id: int):
    """Predeci el resultado de un partido
    Pre: necesita un id de un partido que exista
    Post: devuelva la prediccion de este partido
    Args:
        id (int): identificador del partido

    Returns:
        PrediccionPartido: modelo a devolver
    """
    return PrediccionPartido
