"""
Aqui van los modelos correspondientes al endpoint, ruta o recurso partidos
 
"""
class PartidoBase:
    def __init__(self, equipo_local, equipo_visitante, fecha, fase):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.fase = fase

    def to_dict(self):
        return {
            "equipo_local": self.equipo_local,
            "equipo_visitante": self.equipo_visitante,
            "fecha": self.fecha,
            "fase": self.fase
        }


class Partido(PartidoBase):
    def __init__(self, id, equipo_local, equipo_visitante, fecha, fase, resultado=None):
        super().__init__(equipo_local, equipo_visitante, fecha, fase)
        self.id = id
        self.resultado = resultado

    def to_dict(self):
        data = super().to_dict()
        data["id"] = self.id

        if self.resultado:
            data["resultado"] = self.resultado.to_dict()

        return data

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