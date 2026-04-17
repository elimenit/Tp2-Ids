import requests

# Casos Vacio (400) 
# Faltan alguno o mas campos

URL = "http://localhost:5000/usuarios"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br"}

def test_obtener_usuario_fuera_rango():
    for id in range(0, -10, -1):
        response = requests.get(url=f"{URL}/{id}")
        assert response.status_code == 400

def test_crear_usuario_con_un_campo_vacio():
    usuario_valido = {
        "nombre": "UsuarioTest",
        "email": "Example@.com"}

    for clave in usuario_valido:
        response = requests.post(url=f"{URL}", json={clave: f"{usuario_valido[clave]}"}, headers=HEADERS, timeout=0.5)
        assert response.status_code == 400
    
def test_actualizar_usuario_id_fuera_rango():
    usuario_valido = {
        "nombre": "UsuarioTest",
        "email": "Example@.com"}
    
    valores_invalidos = [-10, -5, 0]
    for id in valores_invalidos:
        response = requests.put(url=f"{URL}/{id}", json={usuario_valido}, headers=HEADERS, timeout=0.5)
        assert response.status_code == 400

def test_actualizar_parcial_usuario_id_fuera_rango():
    usuario_valido = {
        "nombre": "UsuarioTest",
        "email": "Example@.com"}
    
    valores_invalidos = [-10, -5, 0]
    for id in valores_invalidos:
        response = requests.patch(url=f"{URL}/{id}", json=usuario_valido, headers=HEADERS, timeout=0.4)
        assert response.status_code == 400
    
def test_actualizar_parcial_usuario_valores_vacios():
    """ Actualizar usuario con valores vacios
    id: debe ser un valor existente en la Base de Datos
    """
    usuario = {
        "nombre": "Example",
        "email": "example@gmail.com"
    }
    id = 2
    for clave in usuario:
        response = requests.patch(url=f"{URL}/{id}", json={clave: usuario[clave]} ,headers=HEADERS, timeout=0.5)
        assert response.status_code == 400

def test_eliminar_usuario():
    valores_invalidos = [-10, -5, 0]
    for id in valores_invalidos:
        response = requests.delete(url=f"{URL}/{id}", headers=HEADERS, timeout=0.5)
        assert response.status_code == 400


# Error 404 (No Encontrado) 
# 200 (OK)