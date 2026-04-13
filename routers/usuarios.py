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
from database.usuarios import db_crear_usuario

bp_usuarios = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@bp_usuarios.route(rule="/", methods=["GET"])
def listar_usuarios(limit: int =10, offset: int =10):
    """ Lista los usuarios con paginacion
    Pre: Necesita que hayga datos en labase de datos
    Post: Devuelva una lista de usuarios
    """
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
