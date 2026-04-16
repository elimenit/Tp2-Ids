"""
Implementacion de los Endpoint de Usuarios:
# usuarios
GET /usuarios
POST /usuarios
# Por id
GET /usuarios/<id>
PUT /usuarios/<id>
DELETE /usuarios/<id>
# Final 
PAGINACION (limit-offset)
"""
from flask import Blueprint, jsonify, request
from schemas.usuario import UsuarioBase, Usuario
# Validaciones
from seeds.usuarios import validacion_creacion_usuario
# BD
from database.usuarios import db_crear_usuario, db_obtener_usuarios, db_obtener_usuario
# para la paginacion
from utils.paginacion import crear_response_paginacion
# para errores
from utils.errores import error_response

bp_usuarios = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@bp_usuarios.route(rule="/", methods=["GET"])
def listar_usuarios():
    """ Lista los usuarios con paginacion
    Pre: Necesita que halla datos en labase de datos
    Post: Devuelva una lista de usuarios
    """
    limit = request.args.get("_limit", default=10, type=int)
    offset = request.args.get("_offset", default=0, type=int)

    base = request.base_url
    try:
        users_data = db_obtener_usuarios()
    except Exception as e:
        return error_response(
            "Error del servidor",
            "INTERNAL_SERVER_ERROR",
            f"Ha ocurrido un error durante la obtención de usuarios: {e}",
            500
        )
    num_users = len(users_data)
    if offset >= num_users:
        return error_response(
            "Error de input",
            "INVALID_OFFSET",
            f"Ingrese un offset menor a {num_users}",
            400 
        )
    
    selected_users = users_data[offset:(limit+offset)]
    list_users = [{'id': userid, 'nombre': name} for userid, name, _ in selected_users]
    response_pages = crear_response_paginacion(limit, offset, num_users, base)
    response = {
        "metadata": {
            "cant_usuarios": len(users_data)
        },
        "usuarios": list_users,
        "_links": response_pages
    }
    return jsonify(response), 200

@bp_usuarios.route(rule="/<int:input_id>", methods=["GET"])
def listar_usuario(input_id):
    """ 
    Recibido un ID de usuario, devuelve su información
    """
    try:
        users_data = db_obtener_usuarios()
    except Exception as e:
        return error_response(
            "Error del servidor",
            "INTERNAL_SERVER_ERROR",
            f"Ha ocurrido un error durante la obtención de usuarios: {e}",
            500
        )
    lista_ids = [x[0] for x in users_data]
    if (input_id not in lista_ids) or (input_id <= 0):
        return error_response(
            "Input error",
            "ERROR_NOT_FOUND",
            f"No se han encontrado coincidencias para el ID: {input_id}. Ingrese un numero entre {min(lista_ids)} a {max(lista_ids)}.",
            404
        )
    for id, user, email in users_data:
        if id == input_id:
            return {
                "id": id,
                "nombre": user,
                "email": email
            }, 200

@bp_usuarios.route(rule="/", methods=["POST"])
def crear_usuario():
    """Agrega un usuario en la Base de datos
    Pre: el usuario tiene que ser valido
    Post: Agrega un usuario a la Base de datos
    """
    body: dict = request.get_json()
    nombre_usuario = body.get("nombre", None)
    email_usuario = body.get("email", None)
    
    usuario_crear = UsuarioBase(nombre=nombre_usuario, email=email_usuario)
    
    if validacion_creacion_usuario(usuario_crear): 
        usuario = db_crear_usuario(usuario_crear)

        return jsonify({
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email
        }), 201

    return jsonify({"error": "Usuario invalido"}), 400

@bp_usuarios.route(rule="/<int:id>", methods=["PUT"])
def editar_usuario(id: int):
    """ Editar un usuario
    Pre: se debe verificar que el usuario recibido sea valido 
    Post: cambia los valores correspondientes a los campos correspondientes
    Args:
        id (int): id del usuario y debe estar dentro de un rango valido
    """
    pass

@bp_usuarios.route(rule="/<int:id>", methods=["DELETE"])
def eliminar_usuario(id: int):
    """Elimina un usuario
    Pre: El id debe ser valido y existente de un usuario
    Post: Elimina el usuario por su id en la BD.
    Args:
        id (int): id del usuario
    """
    pass
