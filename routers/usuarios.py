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
    users_data = db_obtener_usuarios()
    num_users = len(users_data)
    if offset >= num_users:
        return error_response(
            "OFFSET INVALIDO",
            "INPUT ERROR",
            f"Ingrese un offset menor a {num_users}",
            400
        )
    
    selected_users = users_data[offset:(limit+offset)]
    list_users = [{'id': userid, 'nombre': name} for userid, name in selected_users]
    response_pages = crear_response_paginacion(limit, offset, num_users, base)
    response = {
        "metadata": {
            "cant_usuarios": len(users_data)
        },
        "usuarios": list_users,
        "_links": response_pages
    }
    return jsonify(response), 200

@bp_usuarios.route(rule="/", methods=["GET"])
def listar_usuario():
    """ 
    Recibido un ID de usuario, devuelve su información
    """

    usuarios = db_obtener_usuarios()
    pass

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
