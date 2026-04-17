from flask import jsonify

def error_response(message: str, code: str = "ERROR", description: str = "", status_code: int = 400):
    """Genera una respuesta de error con el formato definido en el swagger
    
    Args:
        message (str): Mensaje corto del error
        code (str): Código identificador del error
        description (str): Descripción detallada del error
        status_code (int): Código HTTP a devolver
    
    Returns:
        Response: Respuesta Flask con formato de error estándar
    """
    return jsonify({
        "errors": [{
            "code": code,
            "message": message,
            "level": "error",
            "description": description
        }]
    }), status_code