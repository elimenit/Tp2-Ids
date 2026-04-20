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
from seeds.usuarios import validacion_creacion_usuario, validacion_campos_usuario
from seeds.usuarios import validacion_offset_limit, validacion_id_usuario
# BD
from database.usuarios import (
    db_crear_usuario, db_obtener_usuarios, db_obtener_usuario,
    db_actualizar_usuario, db_eliminar_usuario
)
# Errores
from utils.errores import error_response

bp_usuarios = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@bp_usuarios.route(rule="/", methods=["GET"])
def listar_usuarios():
    """Lista los usuarios con paginacion
    Pre: Necesita que halla datos en labase de datos
    Post: Devuelva una lista de usuarios

    Returns:
        _type_: _description_
    """
    limit = request.args.get("_limit", default=10, type=int)
    offset = request.args.get("_offset", default=0, type=int)
    if not validacion_offset_limit(limit, offset):
        return error_response(
            code="400",
            message="Limit o Offset no validos",
            level="BAJO",
            description="Limit o Offset invalidos",
            status_code=400
        )
    return jsonify(db_obtener_usuarios(limit, offset)), 200

@bp_usuarios.route(rule="/<int:id>", methods=["GET"])
def obtener_usuario(id):
    """ 
    Recibido un ID de usuario, devuelve su información
    """
    if not validacion_id_usuario(id):
        return error_response(
            "400",
            "id fuera de rango",
            "BAJO",
            "id no valido",
            400)

    user = db_obtener_usuario(id)
    if user is None:
        return error_response(
            "404",
            "El usuario no existe",
            "Alto",
            "Usuario no existente",
            404)
        
    return jsonify(user.to_dict()), 200

@bp_usuarios.route(rule="/", methods=["POST"])
def crear_usuario():
    """Agrega un usuario en la Base de datos
    Pre: el usuario tiene que ser valido
    Post: Agrega un usuario a la Base de datos
    """
    body: dict = request.get_json()
    if body is None or not body:
        return error_response(
            code="400",
            message="Body vacio",
            level="MEDIO",
            description="Body esta vacio",
            status_code=400
        )
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

    return error_response(
        code="400",
        message="Campos no validos",
        description="el usuario ingreso uno de los campos invalidos",
        level="GRAVE",
        status_code=400
    )

@bp_usuarios.route(rule="/<int:id>", methods=["PUT"])
def editar_usuario(id: int):
    """ Editar un usuario
    Pre: se debe verificar que el usuario recibido sea valido 
    Post: cambia los valores correspondientes a los campos correspondientes
    Args:
        id (int): id del usuario y debe estar dentro de un rango valido
    """
    if not validacion_id_usuario(id):
        return error_response(
            code="400",
            message="Id fuera de Rango",
            level="BAJO",
            description="Usuario Invalido",
            status_code=400
        )
    body = request.get_json()
    if body is None or not body:
        return error_response(
            code="400",
            message="Body vacio",
            level="MEDIO",
            description="Body esta vacio",
            status_code=400
        )
    nombre = body.get("nombre", None)
    email = body.get("email", None)
    user = Usuario(id, nombre, email)

    if not validacion_campos_usuario(user):
        return error_response(
            code="400",
            message="Campo no valido",
            level="ALTO",
            description="Uno o mas campos no validos",
            status_code=400
        )
    usuario = db_actualizar_usuario(user)
    return jsonify(usuario.to_dict()), 200
    
@bp_usuarios.route(rule="/<int:id>", methods=["DELETE"])
def eliminar_usuario(id: int):
    """Elimina un usuario
    Pre: El id debe ser valido y existente de un usuario
    Post: Elimina el usuario por su id en la BD.
    Args:
        id (int): id del usuario
    """
    if not validacion_id_usuario(id):
        return error_response(
            code="400",
            message="Id fuera de Rango",
            level="ALTO",
            description="Usuario Invalido",
            status_code=400
        )
    usuario = db_eliminar_usuario(id_user=id)
    if usuario is None or not usuario:
        return error_response(
            code="400",
            message="Usuario no existe",
            level="GRAVE",
            description="el usuario aun no existe",
            status_code=400
        )
    return jsonify(usuario.to_dict()), 200
