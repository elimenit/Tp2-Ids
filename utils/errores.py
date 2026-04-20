from flask import jsonify

def error_response(code: str,  message: str, level: str, description: str, status_code: int = 400):
    """Modelo de Respuesta de la API

    Args:
        code (str): Codigo de estado de la peticion
        message (str): Mensaje corto del error
        level (str): Nivel de riesgo (bajo, alto o grave) del error
        description (str): Motivo del error
        status_code (int, optional): Codigo HTTP a devolver. Defaults to 400.
    """
    return  jsonify({
        "errors": [{
            "code": code,
            "message": message,
            "level": level,
            "description": description
        }]
    }), status_code