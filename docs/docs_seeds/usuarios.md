# Verificacion de /Usuarios

Se valido el ingreso del usuario absolutamente Todo.
## Verificacion en GET /usuarios
...
## Verificacion en POST /usuarios
Se valida que el usuario a insetar en la DB sea valido
Obtenemos la informacion recibida:
Body: 
"""
body = request.json()
"""
Query Params
param1: parametro recibido, toma el valor de la clave correspondiente a "param1"
y si no lo encuentra toma el valor de "value_default".
"""
param1 = request.args.get("param1", "value_default)
"""
Path parameters
esto se estable en el endpoint en si

# Verificacion en PUT /usuarios/{id}
...
# Verificacion en Patch /usuarios/{id}
...
# Verificacion en DELETE /usuarios/{id}
...