"""
Aqui van los modelos correspondientes al endpoint, ruta o recurso partidos
 
"""
class PartidoBase():
    pass

class Partido(PartidoBase):
    """ Tda Partido 
    Representa un partido.
    Args:
        PartidoBase (_type_): Clase base de la que hereda sus atributos
    """

class ResultadoPartido():
    def __init__(self, local: int, visitante: int):
        self.local = local
        self.visitante = visitante
    
    def to_dict(self):
        return {
            "local": self.local,
            "visitante": self.visitante
        }

class PrediccionPartido():
    """TDA de la prediccion de un partido
    """