# Libreria requests de python (HTTP for Humans)
Requests es una libreria cliente HTTP para el lenguaje de Programacion de Python
documentacion: <a href="https://requests.readthedocs.io/en/latest/">libreria requests</a>
## methods HTTP
Para interactuar con los verbos http(get, post, ...) con requests usamos las funciones de requests:
get, post, ... que nos ayudaran en la creacion de la solicitud
### method get()
Para realizar una peticion del tipo get con requests 
´´´
response = requests.get(url="example.com", headers={}, timeout=0.1)
print(response.status_code) # vemos el estado de la respuesta
