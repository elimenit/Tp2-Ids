# TDA (Tipo de dato Abstracto) o TAD (Tipo Abstracto de dato)
Un TDA o TAD es una estructura que busca modelar algo
Ejemplo:
Queremos modelar un usuario que tiene como atributos identificador, nombres y apellidos
´´´
class Usuario():
    identificador: int
    nombres: str
    apellidos: str
´´´
# Identico VS Iguales en python
Se dice que dos Objetos son iguales si tienen el mismo contenido:
´´´
a = 5
b = a # Iguales
b = 6
print(a == b) # False
´´´
se dice que dos objetos son identicos si al modificar a uno altera al otro:
´´´
class User():
    nombre = "hola"
    def __init__(self, nombre)-> None:
        self.nombre = nombre
a = User("Pepito")
b = a # Identicos
b.nombre = "Purpura"
print( a == b ) # True
´´´
