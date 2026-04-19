"""
Aqui van los modelos correspondientes al endpoint, ruta o recurso partidos
 
"""
class PartidoBase():
    equipo_local: str
    equipo_visitante: str
    fecha: str
    fase: str
    def __init__(self, equipo_local: str, equipo_visitante: str, fecha: str, fase: str):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.fase = fase

class Partido(PartidoBase):
    id: int
    resultado: dict[str, int]
    def __init__(self, id: int, resultado: dict[str, int], equipo_local: str, equipo_visitante: str, fecha: str, fase: str):
        super().__init__(equipo_local, equipo_visitante, fecha, fase)
        self.id = id
        self.resultado = resultado

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "equipo_local": self.equipo_local,
            "equipo_visitante": self.equipo_visitante,
            "fecha": self.fecha,
            "fase": self.fase,
            "resultado": {
                "local": self.resultado.get("local"),
                "visitante": self.resultado.get("visitante")
            }
        }
    
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