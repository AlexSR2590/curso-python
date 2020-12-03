"""
Escribir un programa que añada valores a una lista
mientras que su longitud sea menor que 20 y luego mostrar la lista
usar while y for
"""
cosas = []
cosas2 = []

longLista = len(cosas)

print("*****Usando ciclo While*****\n")
while longLista < 20:
	nuevo_elemento = input("Introduce un elemento a la lista: ")
	cosas.append(nuevo_elemento)
	longLista += 1
else:
	print("Ya no caben más elementos en la lista")
	print(cosas)

print("---------------------------------\n")

print("*****Usando ciclo for*****")

for i in range(20):
	nuevo_elemento2 = input("Introduce un elemento a la lista: ")
	cosas2.append(nuevo_elemento2)
	i += 1
else:
	print("Ya no caben más elementos en la lista")
	print(cosas2)


""""
#Ciclo for
coleccion = []

for contador in range(0,120):
	coleccion.append(f"elemento-{contador}")
	print("Mostrando el: " +  coleccion[contador])

print(coleccion)
""""
"""
#Ciclo while

coleccion = []
x = 0
while x <20:
	coleccion.append(f"Elemento-{x}") 
	print("Mostrando el:" + coleccion[x])
	x += 1

print(coleccion)
"""

