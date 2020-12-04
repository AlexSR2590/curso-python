"""
Crear un Script que tenga 4 variables
lista
string
entero
booleano
Imprimir un mensaje según el tipo de dato de 
cada variable
"""
def traducirTipo(tipo):
	result = None
	if tipo == list:
		result = "LISTA"
	elif tipo == int:
		result = "ENTERO"
	elif tipo == bool:
		result = "BOOLEANO"
	elif tipo == float:
		result = "FLOTANTE"
	elif tipo == str:
		result = "CADENA DE TEXTO"
	return result
	

def comprobarTipoVariable(variable):
	if isinstance(variable, list):
		return "La variable es una lista!"
	elif isinstance(variable, str):
		return "La variable es un string!"
	elif isinstance(variable, bool):
		return "La variable es un booleano"
	elif isinstance(variable, int):
		return "La variable es un entero"

def comprobarTipado(dato, tipo):
	test = isinstance(dato, tipo)
	result = ""

	if test:
		result = f"Este dato es de tipo {traducirTipo(tipo)}"
	else:
		result = f"El tipo de dato no corresponde"
	return result

lista = []
string = ""
entero = 0
booleano = False

print(comprobarTipoVariable(lista))
print(comprobarTipoVariable(string))
print(comprobarTipoVariable(entero))
print(comprobarTipoVariable(booleano))
print("-----------------------------")
print(comprobarTipado(lista, list))
print(comprobarTipado(entero, int))
