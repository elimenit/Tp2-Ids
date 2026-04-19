"""
Usamos pytest
Probamos al endpoint /partidos
Pre: Base de datos vacia
Post: todos los test deben de pasar
"""
import requests

URL = "http://localhost:5000/partidos"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "application/json"
}
# GET
## 200
def test_obtener_partidos():
    response = requests.get(url=f"{URL}", headers=HEADERS)
    assert response.status_code == 200

def test_obtener_partido():
    partido = {
    "equipo_local": "Argentina",
    "equipo_visitante": "Brasil",
    "fecha": "2025-05-19",
    "fase": "GRUPOS"
    }
    response = requests.post(url=URL, json=partido, headers=HEADERS)
    assert response.status_code == 201
    
    user_created = response.json() 
    response = requests.get(url=f"{URL}/{user_created["id"]}", headers=HEADERS)
    assert response.status_code == 200
    
    get_user = response.json()
    for key in get_user:
        assert get_user[key] == user_created[key]
    
    response = requests.delete(url=f"{URL}/{user_created["id"]}", headers=HEADERS)
    assert response.status_code == 200


## 404
# POST
## 201
def test_crear_partido():
    partido = partido = {
    "equipo_local": "Argentina",
    "equipo_visitante": "Brasil",
    "fecha": "2025-05-19",
    "fase": "FINAL"
    }
    response = requests.post(url=f"{URL}", json=partido, headers=HEADERS)
    assert response.status_code == 201
    
    id_partido = response.json()["id"]
    response = requests.delete(url=f"{URL}/{id_partido}", headers = HEADERS)
    assert response.status_code == 200

def test_actualizar_resultado():
    partido = {
    "equipo_local": "Alemania",
    "equipo_visitante": "Portugal",
    "fecha": "2026-04-19",
    "fase": "SEMIS"
    }
    resultado = {
        "local": 2,
        "visitante": 1
    }
    response = requests.post(url=f"{URL}", json=partido, headers=HEADERS)
    assert response.status_code == 201

    id_partido = response.json()["id"]
    response = requests.put(url=f"{URL}/{id_partido}/resultado", json=resultado, headers=HEADERS)
    assert response.status_code == 200
    partido_update = response.json()
    for key in resultado:
        assert resultado[key] == partido_update["resultado"][key]

## 400
def crear_partido_vacio():
    """Intenta crear un partido con contenido vacio
    """
    content_boby = {}
    empty_partido = requests.post(url=f"{URL}", headers=HEADERS, json=content_boby, timeout=0.5)
    assert empty_partido.status_code == 400
## 404  
# PUT 
## 200
## 400
## 404
# PATCH
## 200
## 400
## 404
# DELETE
# 200
# 404

# Partidos Casos Vacios