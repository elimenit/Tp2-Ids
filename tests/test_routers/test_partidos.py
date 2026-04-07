"""
Usamos pytest
Probamos al endpoint /partidos
Pre: Base de datos vacia
Post: todos los test deben de pasar
"""
import requests

URL_PARTIDOS = "localhost:5000/partidos"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br"}

# Partidos Casos Vacios
def crear_partido_vacio():
    """Intenta crear un partido con contenido vacio
    """
    content_boby = {}
    empty_partido = requests.post(url=URL_PARTIDOS, headers=HEADERS, json=content_boby, timeout=0.5)
    assert empty_partido.status_code == 400

def crear_partido_campos_vacios():
    """Intenta crear un partido con uno de los campos vacios
    Pre: Necesita que no exista este equipo
    Post: no deberia de poder crearse un equipo con uno de los camos vacios
    """
    example_partido: dict = {
        "equipo_local": "Argentina",
        "equipo_visitante": "Brasil",
        "fecha": "2025-05-19",
        "fase": "GRUPOS"
    }
    for key in example_partido:
        copia_partido = example_partido # Concepto de son iguales o identicos
        copia_partido[key] = ""
        intent_created_partido = requests.post(url=URL_PARTIDOS, headers=HEADERS, json=copia_partido, timeout=0.3)
        assert intent_created_partido.status_code == 400

def obtener_partido_vacio():
    """Valida que la Base de datos este vacia
    """
    partido_vacio = requests.get(url=URL_PARTIDOS, headers=HEADERS, timeout=0.5)
    assert partido_vacio.status_code == 200
    assert isinstance(partido_vacio.json(), list)
    assert len(partido_vacio.json()) == 0

def 
# Partidos Casos Ideales

def test_crear_partido(): # Porfavor si no va ha retornar nada no coloquen None
    """Test de la funcion crear de un partido
    """
    expected_partido: dict = {
        "equipo_local": "Argentina",
        "equipo_visitante": "Brasil",
        "fecha": "2025-05-19",
        "fase": "GRUPOS"
    }
    
    partido_creado = requests.post(url=f"{URL_PARTIDOS}", json=expected_partido, headers=HEADERS, timeout=0.5)
    assert partido_creado.status_code == 201
    partido = partido_creado.json()
    assert partido == expected_partido 
    
    for campo in expected_partido:
        assert expected_partido[campo] == partido[campo]

def test_obtener_partido():
    """
    Prueba si un equipo se crea y se obtiene el equipo
    """
    expected_partido: dict = {
        "equipo_local": "Peru",
        "equipo_visitante": "Argentina",
        "fecha": "2025-05-19",
        "fase": "GRUPOS"
    }
    
    partido_creado = requests.post(url=f"{URL_PARTIDOS}", json=expected_partido, headers=HEADERS, timeout=0.5)
    assert partido_creado.status_code == 201
    id_partido = partido_creado.json()["id"]
    partido_obtenido = requests.get(url=f"{URL_PARTIDOS}/{id_partido}", headers=HEADERS, timeout=0.5)
    partido = partido_obtenido.json()
    
    for campo in expected_partido:
        assert expected_partido[campo] == partido[campo]

def test_listar_partido():
    """Verificamos que se obtenga una lista de partidos
    """
    listado_partidos = requests.get(url=URL_PARTIDOS, headers=HEADERS, timeout=0.5)
    assert listado_partidos.status_code == 200
    assert isinstance(listado_partidos.json(), list)
        
def test_actualizar_partido():
    """Verifica que la actualizacion de cada campo se realiza correctamente
    Pre: El edpoint exista
    Post: prueba crear con uno hasta con todos los campos vacios
    """
    initial_partido: dict = {
        "equipo_local": "Argentina",
        "equipo_visitante": "inglaterra",
        "fecha": "2025-05-19",
        "fase": "GRUPOS"
    }
    update_partido: dict = {
        "equipo_local": "Alemania",
        "equipo_visitante": "Rusia",
        "fecha": "2025-04-20",
        "fase": "FINAL"
    }

    partido_creado = requests.post(url=f"{URL_PARTIDOS}", json=expected_partido, headers=HEADERS, timeout=0.5)
    assert partido_creado.status_code == 201 
    id_partido = partido_creado.json()["id"]
    partido_actualizado = requests.put(url=f"{URL_PARTIDOS}/{id_partido}", json=update_partido, headers=HEADERS, timeout=0.5)
    assert partido_actualizado.status_code == 200

    for campo in update_partido:
        assert partido_actualizado.json()[campo] == update_partido[campo] # Identicos 



def actualizar_parcialmente_partido():
    def verificar_campo_actualizado(url, key_campo, value_campo):
        """ usada como funcion privada que actualiza cada uno de los campos

        Args:
            url (_type_): url peticion
            key_campo (_type_): clave del body a actualizar
            value_campo (_type_): valor del campo
        """

        partido_actualizado = requests.put(url=url, json={key_campo: value_campo}, headers=HEADERS, timeout=0.5)
        assert partido_actualizado.status_code == 200
        assert partido_actualizado.json()[key_campo] == value_campo 
    
    initial_partido: dict = {
        "equipo_local": "Argentina",
        "equipo_visitante": "Chile",
        "fecha": "2025-05-19",
        "fase": "GRUPOS"
    }
    
    update_partido: dict = {
        "equipo_local": "India",
        "equipo_visitante": "China",
        "fecha": "2025-04-19",
        "fase": "SEMIFINAL"
    }
    
    created_intial_partido = requests.post(url=URL_PARTIDOS, json=initial_partido, headers=HEADERS, timeout=0.5)
    assert created_intial_partido.status_code == 200
    id_partido = created_intial_partido.json("id")

    for key_campo in update_partido:
        verificar_campo_actualizado(url=f"{URL_PARTIDOS}/{id_partido}", key_campo=key_campo, value_campo=update_partido.get(key=key_campo))
    
    partido_modificado = requests.get(url=f"{URL_PARTIDOS}/{id_partido}", headers=HEADERS, timeout=0.5)
    
    assert partido_modificado.status_code == 200
    assert partido_modificado.json() == update_partido


def test_eliminar_partido():
    initial_partido: dict = {
        "equipo_local": "United States",
        "equipo_visitante": "United Kingdom",
        "fecha": "2026-05-19",
        "fase": "CUARTOS"
    }
    partido_creado = requests.post(url=f"{URL_PARTIDOS}", json=initial_partido, headers=HEADERS, timeout=0.5)
    assert partido_creado.status_code == 201
    assert partido_creado.json() == initial_partido
    id_partido = partido_creado.json()["id"]
    partido_eliminado = requests.delete(url=f"{URL_PARTIDOS}/{id_partido}", headers=HEADERS, timeout=0.5)
    assert partido_eliminado.status_code == 200
    for key_campo in initial_partido:
        assert partido_eliminado.json()[key_campo] == initial_partido[key_campo]
