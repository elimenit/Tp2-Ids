"""
Aqui va una informacion acerca de este modulo:
# Estilo de codigo PEP8 y los zens de python
Sintaxis de la declaracion de un variable:
	variable: tipo = valor
	# variable: es el nombre de una variable
	# tipo: especificamos el tipo de dato que deberi corresponder a la variable
	# valor: valor que asume la variable 
	
Valores que puede tomar el tipo de dato de una variable
byte -> Para uso de bytes
int -> Entero
float -> Valor flotante o de coma decimal
str -> Cadena de texto (Strings)

list -> Lista o arreglo de elementos (No especificamos los elementos de la lista) # Encarecidamente NO usar
set -> conjunto de elementos (No estan ordenados) # Usar con cuidado
dict -> Diccionario o Hash de elementos que corresponden a clave -valor ()  # Por favor NO usar sin especificar el dato de la clave y valor
# Para usar listas, conjuntos y diccionarios
+ list[int] -> Lista de elementos enteros
+ list[str] -> lista de elementos string
+ list[dict[int, str]] -> lista de diccionarios que tienen como clave valores enteros y valor strings
+ dict[int, int] -> diccionario o hash que tiene como clave y valor elementos enteros
+ dict[int, str] -> diccionario o hash que tiene como clave un entero y valor un string

Que pasa si usamos POO ?
La respuesta no varia porque si tenemos la clase Usuario, Partido y mas:
usuarios: list[Usuario] -> usuarios es una lista de la clase o entidad Usuario
partidos: list[Partido] -> partidos es una lista de la clase o entidad Partido

## Opcional (Si lo visto arriba falla)
Usar la libreria typing para el tipo de datos ya que nos ofrece los tipos
de datos list, dict, set y mas como Objetos (Dict, List, Set y mas):
from typing import Dict
Dict[int, [Usuario, Partido]] -> es un diccionario o hash que tiene como clave un numero entero y valor una lista 
	que indica  que en la pocicion 0 y 1 se encuentra las entidades correspondientes a Usuario y Partido respectivamente. 

"""
# Usemos Type-Hints para establecer el tipo de dato que debe ser una variable
def funcion(parametros: list[int]) -> int:
	resultado: int = 0
	"""
	Documentacion de lo que hace esta funcion
	Pre: que es lo que necesita esta funcion para funcionar
	Post: Que es lo que hace esta funcion
		Documentacion de los parametros
		parametros: parametros de la funcion (lista de enteros)
		return: devuelve el resultado de la funcion (entero)
	"""
	# Validacion de los parametros
	if not isinstance(parametros, list[int]):
		"""
		isinstance(variable) -> True : si la variable <varibable> corresponde al tipo de dato <tipo>
		"""
	
		"""
		Lanzamos una excepcion porque no se cumple con lo esperado y dejamos la responsibilidad de atrapar esta excepcion
		a la funcion que haga uso de esta funcion, esto se replica para cada uno de los parametros y segun que tipo de error
		genere es el que deberiamos lanzar
		"""
		raise ValueError("los argumentos son invalidos no cumplen precondiciones")
		
	return resultado;
# Como seria en los test de una funcion
def test_funcion():
	"""
	test de la funcion del paquete <paquete> y modulo  <modulo> (sin el .py) correspondiente a la funcion <funcion>
	el nombre de esta funcion debe ser test_<funcion>.
	¿Que valida esta funcion? ->  debes indicarlo claramente
	"""
	# como vamos ha usar pytest
	try:
		lista: list[str] = ["Hola", "mundo"]
		funcion(lista) # esto deberia lanzar un ValueError
	except ValueError as e:
		print("La funcion promete lo que se esperaba")
	except Exception as e:
		print(f"La funcion no cumple con lo esperado: {str(e)}")

# Y como seria la estructura de una entidad o clase:
class Usuario():
	"""
	Informacion acerca de la entidad que queremos modelar del mundo real
	"""
	id: int # los atributos deben ser las caracteristicas del mundo real
	nombre: str
	legajo: int
	partidos_jugados: int
	partidos_ganados: int
	partidos_perdidos: int
	
