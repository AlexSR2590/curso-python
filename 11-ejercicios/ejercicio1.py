"""
Hcaer un programa que tenga una lista de 8 numeros enteros
y hacer lo siguiente:
- Recorrer la lista y mostrarla
- Ordenar la lista y mostrarla
- Mostrar su longitud
- Bucar algun elemento que el usuario pida por teclado
"""

numeros = [1, 9, 4, 2, 30, 7, 28, 18]

#Recorrer la lista y mostrarla (función)
print("Recorrer la lista y mostrarla")
def recorrerLista(lista):
	resultado = ""
	for numero in lista:
		resultado += "\n" + str(numero)
	return resultado

print(recorrerLista(numeros))
print("------------------------\n")

#Ordernar la lista y mostrarla (función)
print("Ordenar lista")
def ordernarLista(lista):
	lista.sort()
	return lista

print(ordernarLista(numeros))
print("------------------------\n")

#Mostrar longitud de la lista
print("Mostar longitud de la lita")
print(len(numeros))
print("------------------------\n")

#Buscar algún elemento que pida el usuario
print("Buscar elemento en la lista\n")
encontrado = False
def buscarElemento(lista, encontrar):
	if encontrar in lista:
		return True
	else:
		return False

while encontrado == False:
	encontrar = int(input("¿Qué número quieres buscar?: "))
	encontrado = buscarElemento(numeros, encontrar)
	if encontrado == False:
		print("Número no encontrado en la lista\n")
	else:
		print("Número encontrado en la lista en el índice: ")
		print(numeros.index(encontrar))

"""
print("Buscar elemento en la lista")

busqueda = int(input("Introduce un número: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
	busqueda = int(input("introduce un númro: "))
else:
	print(f"Has introducido el {busqueda}")
print(f"#### Buscar en la lista el número {busqueda} #####")

search = numeros.index(busqueda)
print(f"El número buscado existe en el indice: {search}")
"""