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
from schemas.partido import (
    Partido, ResultadoPartido, PrediccionPartido
)
# Validaciones
from seeds.partidos import (
    validar_fecha, validar_offset_limit, validar_id_partido
)
# conexion con la Base de datos
from database.partidos import (
    db_obtener_partidos, db_obtener_partido, db_crear_partido,
    db_actualizar_partido, db_actualizar_parcialmente_partido, db_eliminar_partido,
    db_obtener_prediccion, db_actualizar_resultado
)

from utils.errores import error_response

bp_partidos = Blueprint('partidos', __name__, url_prefix='/partidos') 

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
    equipo = request.args.get("equipo", None)
    fecha = request.args.get("fecha", None)
    fase = request.args.get("fase", None)
    limit = request.args.get("_limit", 10, type=int)
    offset = request.args.get("_offset", 0, type=int)
    if fecha and not validar_fecha(fecha):
        return error_response(
            code="400",
            message="Fecha no valida",
            level="Medio",
            description="Fecha no serializable",
            status_code=400
        )
    if not validar_offset_limit(limit, offset):
        return error_response(
            code="400",
            message="Limit u Offset no validos",
            level="Alto",
            description="Limit u offset no validos",
            status_code=400
        )
    results = db_obtener_partidos(equipo, fecha, fase, limit, offset)
    print(f"Valor")
    print(type(results))
    print("---")
    if results is None:
        return jsonify([]), 200
    return jsonify(results), 200

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
    if not validar_id_partido(id):
        return error_response(
            code="400",
            message="Id no valido",
            level="BAJO",
            description="Id no valido",
            status_code=400
        )
    partido = db_obtener_partido(id)
    if partido is None:
        return error_response(
            code="404",
            message="Partido Not Found",
            level="ALTO",
            description="Partido no encontrado",
            status_code=404
        )

    return jsonify(partido.to_dict()), 200

@bp_partidos.route("/", methods=["POST"])
def crear():
    """ Creacion de un Partido
    Pre: Recibe en el Body la informacion de un partido
    Post: Devuelve el partido creado

    Returns:
        _type_: devuelve el equipo creado
    """
    body = request.get_json()
    if body is None:
        return error_response(
            code="400",
            message="Campos vacios",
            level="MEDIO",
            description="Campos vacios o nulos",
            status_code=400
        )
    equipo_local = body.get("equipo_local", None)
    equipo_visitante = body.get("equipo_visitante", None)
    fecha = body.get("fecha", None)
    fase = body.get("fase", None)

    if not ( equipo_local and equipo_visitante and fecha and fase ):
        return error_response(
            code="400",
            message="Uno o mas campos vacios",
            level="ALTO",
            description="Campos vacios no es valido",
            status_code=400)  

    equipo_local = equipo_local.strip().lower()
    equipo_visitante = equipo_visitante.strip().lower()
    
    if equipo_local == equipo_visitante:
        return error_response(
            code="400",
            message="Los equipos no pueden ser iguales",
            level="ALTO",
            description="Equipos iguales es invalido",
            status_code=400)

    if not validar_fecha(fecha):
        return error_response(
            code=400,
            message="Fecha no valida",
            level="MEDIO",
            description="Formato de la fecha no valido",
            status_code=400)

    id_partido = db_crear_partido(
        equipo_local, equipo_visitante,
        fecha, fase)

    return jsonify(db_obtener_partido(id_partido).to_dict()), 201

@bp_partidos.route("/<int:id>", methods=["PUT"])
def actualizar(id: int):
    body = request.get_json()
    if body is None:
        return error_response(
            code="400",
            message="Campos vacios",
            level="MEDIO",
            description="Campos vacios o nulos",
            status_code=400)

    equipo_local = body.get("equipo_local", None)
    equipo_visitante = body.get("equipo_visitante", None)
    fecha = body.get("fecha", None)
    fase = body.get("fase", None)

    if not validar_id_partido(id):
        return error_response(
            code="400",
            message="Id no valido",
            level="BAJO",
            description="Id del partido no valido",
            status_code=400
        )
    
    if not ( equipo_local and equipo_visitante and fecha and fase ):
        return error_response(
            code="400",
            message="Uno o mas campos vacios",
            level="ALTO",
            description="Campos vacios no es valido",
            status_code=400)  

    equipo_local = equipo_local.strip().lower()
    equipo_visitante = equipo_visitante.strip().lower()
    
    if equipo_local == equipo_visitante:
        return error_response(
            code="400",
            message="Los equipos no pueden ser iguales",
            level="ALTO",
            description="Equipos iguales es invalido",
            status_code=400)

    if not validar_fecha(fecha):
        return error_response(
            code=400,
            message="Fecha no valida",
            level="MEDIO",
            description="Formato de la fecha no valido",
            status_code=400)
    
    update_partido = db_actualizar_partido(
        id, equipo_local, equipo_visitante,
        fecha, fase
    )
    if update_partido is None:
        return error_response(
            code="404",
            message="Partido No encontrado",
            level="ALTO",
            status_code=404
        )
    return jsonify(db_obtener_partido(id).to_dict()), 200
    

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
    body = request.get_json()
    if body is None:
        return error_response(
            code="400",
            message="Campos vacios",
            level="MEDIO",
            description="Campos vacios o nulos",
            status_code=400
        )
    
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
    if not validar_id_partido(id): 
        return error_response(
            code="400",
            message="id no valido",
            level="BAJO",
            description="Id no valido",
            status_code=400)

    user = db_obtener_partido(id)
    if user is None:
        return error_response(
            code="404",
            message="Partido no existe",
            level="ALTO",
            description="No se encontro el partido",
            status_code=404
        )
    if db_eliminar_partido(id): 
        return jsonify(user.to_dict()), 200
    return error_response(
        code="400",
        message="id invalido",
        level="GRAVE",
        status_code=400
    )
@bp_partidos.route("/<int:id>/resultado", methods=["PUT"])
def actualizar_resultado(id: int):

    if not validar_id_partido(id):
        return error_response(
            code="400",
            message="Id no valido",
            status_code=400
        )

    body = request.get_json()

    if not body:
        return error_response(
            code="400",
            message="Campos vacios",
            status_code=400
        )

    if body.get("local") is None or body.get("visitante") is None:
        return error_response(
            code="400",
            message="Faltan campos",
            status_code=400
        )

    try:
        goles_local = int(body["local"])
        goles_visitante = int(body["visitante"])
    except (TypeError, ValueError):
        return error_response(
            code="400",
            message="Deben ser enteros",
            status_code=400
        )

    updated = db_actualizar_resultado(id, goles_local, goles_visitante)

    if not updated:
        return error_response(
            code="404",
            message="Partido Not Found",
            status_code=404
        )

    partido = db_obtener_partido(id)

    if not partido:
        return error_response(
            code="404",
            message="Partido no encontrado",
            status_code=404
        )

    return jsonify(partido.to_dict()), 200
    
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