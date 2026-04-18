"""
Endpoint de partidos:
GET /partidos
POST /partidos

# por Id
GET /partidos/<id>
DElETE /partidos/<id>

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
from database.db import get_connection
from schemas.partido import (
    Partido, ResultadoPartido, PrediccionPartido
)
from utils.errores import error_response

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

    datos = request.get_json() 

    if not datos:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
    
    # verifico que no hayan campos vacios o faltantes, si los hay devuelvo error.
    campos_obligatorios = ["equipo_local_id", "equipo_visitante_id", "fecha", "fase_id"]
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] is None or datos[campo] == "":
            return jsonify({"error": 'Los campos "equipo_local_id", "equipo_visitante_id", "fecha" y "fase_id" son obligatorios'}), 400

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM partidos WHERE id = %s", (id,))
    if not cursor.fetchone():
        return jsonify({"error": "No se encontro el partido"}), 404
    
    # Verifico que existan los equipos y la fase, si no existen devuelvo error.
    cursor.execute("SELECT * FROM equipos WHERE id = %s", (datos.get("equipo_local_id"),))
    if not cursor.fetchone():
        return jsonify({"error": "El equipo local no existe en la base de datos"}), 404
    
    cursor.execute("SELECT * FROM equipos WHERE id = %s", (datos.get("equipo_visitante_id"),))
    if not cursor.fetchone():
        return jsonify({"error": "El equipo visitante no existe en la base de datos"}), 404
    
    cursor.execute("SELECT * FROM fases WHERE id = %s", (datos.get("fase_id"),))
    if not cursor.fetchone():
        return jsonify({"error": "La fase no existe en la base de datos"}), 404

    query = """
    UPDATE partidos
    SET equipo_local_id = %s, equipo_visitante_id = %s, fecha = %s, fase_id = %s
    WHERE id = %s
    """

    cursor.execute(query, (
        datos.get("equipo_local_id"),
        datos.get("equipo_visitante_id"),
        datos.get("fecha"),
        datos.get("fase_id"),
        id
    ))

    conn.commit()
    
    # Obtengo el partido actualizado para luego returnearlo
    cursor.execute("SELECT * FROM partidos WHERE id = %s", (id,))
    partido_actualizado = cursor.fetchone()

    return jsonify(partido_actualizado), 200

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
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        data = request.get_json()

        if 'local' not in data or 'visitante' not in data:
            return error_response("Faltan campos local o visitante", code="BAD_REQUEST")

        if not isinstance(data['local'], int) or not isinstance(data['visitante'], int):
            return error_response("local y visitante deben ser enteros", code="BAD_REQUEST")

        if data['local'] < 0 or data['visitante'] < 0:
            return error_response("Los goles no pueden ser negativos", code="BAD_REQUEST")

        cursor.execute("SELECT id FROM partidos WHERE id = %s", (id,))
        partido = cursor.fetchone()

        if not partido:
            return error_response("Partido no encontrado", code="NOT_FOUND", status_code=404)

        cursor.execute("SELECT id FROM resultados WHERE partido_id = %s", (id,))
        resultado_existente = cursor.fetchone()

        if resultado_existente:
            cursor.execute(
                "UPDATE resultados SET local = %s, visitante = %s WHERE partido_id = %s",
                (data['local'], data['visitante'], id)
            )
        else:
            cursor.execute(
                "INSERT INTO resultados (partido_id, local, visitante) VALUES (%s, %s, %s)",
                (id, data['local'], data['visitante'])
            )

        conn.commit()
        return '', 204

    except Exception as e:
        conn.rollback()
        return error_response("Error interno del servidor", code="INTERNAL_ERROR", description=str(e), status_code=500)

    finally:
        cursor.close()
        conn.close()

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
    pass