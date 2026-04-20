"""
Los tests deberian ser idenpotentes. 
Los numeros negativos python lo interpreta como stringcarece de sentido usar numeros negativos(PATH Parameters).
"""
import requests

URL = "http://localhost:5000/usuarios"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "application/json"}

# GET
## 200
def test_obtener_usuario():
    user = {
        "nombre": "Juan",
        "email": "gmail@gmail.com"
    }
    response = requests.post(url=f"{URL}", json=user, headers=HEADERS)
    assert response.status_code == 201
    
    user_created = response.json()
    response = requests.get(url=f"{URL}/{user_created["id"]}", headers=HEADERS)
    assert response.status_code == 200
    
    get_user = response.json()
    for key in user_created:
        assert user_created[key] == get_user[key]

## 400
def test_obtener_usuario_nulo():
    response = requests.get(url=f"{URL}/0", headers=HEADERS)
    assert response.status_code == 400

def test_obtener_usuario_no_encontrado(): #ejemplo de valor negativo
    for id in range(-1, -5, -1):
        response = requests.get(url=f"{URL}/{id}")
        assert response.status_code == 404 
## 404

# POST
## 201
def test_crear_usuario():
    usuario_valido = {
        "nombre": "juan",
        "email": "example@gmail.com"
    }
    response = requests.post(url=f"{URL}", json=usuario_valido, headers=HEADERS)
    assert response.status_code == 201

    user_created = response.json()
    id_user = user_created["id"]
    for key in usuario_valido:
        assert usuario_valido[key] == user_created[key]

    response_delete = requests.delete(url=f"{URL}/{id_user}")
    assert response_delete.status_code == 200
    
    user_delete = response_delete.json()
    for key in user_delete:
        assert user_created[key] == user_delete[key]
  
## 400
### Campos Nulos
def test_crear_usuario_con_un_campo_vacio():
    usuario_valido = {
        "nombre": "UsuarioTest",
        "email": "Example@.com"}

    for clave in usuario_valido:
        response = requests.post(url=f"{URL}", json={clave: f"{usuario_valido[clave]}"}, headers=HEADERS)
        assert response.status_code == 400
# PUT
## 200
def test_actualizar_usuario():
    usuario_crear = {
        "nombre": "Pepito",
        "email": "example@gmail.com"
    }
    user_update = {
        "nombre": "Josesito",
        "email": "jose@gmail.com"
    } 
    response = requests.post(url=f"{URL}", headers=HEADERS, json=usuario_crear)
    assert response.status_code == 201
    
    id_user = response.json()["id"]
    resp_update = requests.put(url=f"{URL}/{id_user}", json=user_update, headers=HEADERS)
    assert resp_update.status_code == 200
    
    user_recv = resp_update.json()
    for key in user_update:
        assert user_update[key] == user_recv[key]
    
    response = requests.delete(url=f"{URL}/{id_user}", headers=HEADERS)
    assert response.status_code == 200

## 400
def actualizar_usuario_nulo_sin_body():
    response = requests.put(url=f"{URL}/0", headers=HEADERS)
    assert response.status_code == 400

## 404

# DELETE
## 200
def test_eliminar_usuario():
    user = {
        "nombre": "Jhon Doe",
        "email": "eamil@gmail.com"
    }
    response = requests.post(url=f"{URL}", json=user, headers=HEADERS)
    assert response.status_code == 201
    
    user_created = response.json()
    response = requests.delete(url=f"{URL}/{user_created["id"]}", headers=HEADERS)
    assert response.status_code == 200

    remove_user = response.json()
    for key in user_created:
        assert user_created[key] == remove_user[key]

## 400
def test_eliminar_usuario_nulo_():
    response = requests.delete(url=f"{URL}/0", headers=HEADERS)
    assert response.status_code == 400

#### -----END--------####    
