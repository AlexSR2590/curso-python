"""
Crear un Script que tenga 4 variables
lista
string
entero
booleano
Imprimir un mensaje según el tipo de dato de 
cada variable
"""
lista = []
string = ""
entero = 0
booleano = False

def comprobarTipoVariable(variable):
	if isinstance(variable, list):
		return "La variable es una lista!"
	elif isinstance(variable, str):
		return "La variable es un string!"
	elif isinstance(variable, bool):
		return "La variable es un booleano"
	elif isinstance(variable, int):
		return "La variable es un entero"

print(comprobarTipoVariable(lista))
print(comprobarTipoVariable(string))
print(comprobarTipoVariable(entero))
print(comprobarTipoVariable(booleano))


