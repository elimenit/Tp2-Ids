"""
Endpoint de partidos:
GET /partidos
POST /partidos

# por Id
GET /partidos/<id>"""

from database.conexion import get_conexion

def obtener_partido(id_partido: int):
    conn = get_conexion()
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
from flask import Blueprint
from schemas.partido import (
    Partido, ResultadoPartido, PrediccionPartido
)

bp_partidos = Blueprint('partidos', __name__, url_prefix='/') 

@bp_partidos.route("/", methods=["GET"])
def listar(equipo: str, fecha: str, fase: str, _limit: int, _offset: int) -> list[Partido]:
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
    return list[Partido]

@bp_partidos.route("/", methods=["POST"])
def crear() -> Partido:
    """ Creacion de un Partido
    Pre: Recibe en el Body la informacion de un partido
    Post: Devuelve el partido creado

    Returns:
        _type_: devuelve el equipo creado
    """
    return {} 

@bp_partidos.route("/<int:id>", methods=["GET"])
def obtener(id: int) -> Partido:
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
def actualizar(id: int) -> Partido:
    """Actualiza el partido

    Args:
        id (int): id del partido a actualizar

    Returns:
        Partido: el partido actualizado
    """
    return partido

@bp_partidos.route("/<int:id>", methods=["PATCH"])
def actualizar_parcialmente(id: int)-> Partido:
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
def eliminar(id: int)-> Partido:
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
def mostrar_resultado(id: int) -> ResultadoPartido:
    """Resultado de un partido
    Pre: necesita el id de un partido
    Post: devuelve el resultado de un partido
    Args:
        id (int): Id del partido

    Returns:
        ResultadoPartido: modelo de como resulto un partido
    """
    return ResultadoPartido

@bp_partidos.route("/<int:id>/prediccion", methods=["POST"])
def predecir(id: int) -> PrediccionPartido:
    """Predeci el resultado de un partido
    Pre: necesita un id de un partido que exista
    Post: devuelva la prediccion de este partido
    Args:
        id (int): identificador del partido

    Returns:
        PrediccionPartido: modelo a devolver
    """
    return PrediccionPartido
