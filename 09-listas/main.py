#Listas o arreglos
pelicula = "Batman"
#print(pelicula)

#Definir lista
peliculas = ["Batman", "Spiderman", "Superman"]
animales = list(('Perro', 'Gato', 'Conejo', 'Lobo'))
years = list(range(2020, 2050))
variada = ["Alexis", 29, False, 3.14]

"""
print(animales)
print(peliculas)
print(years)
print(variada)
"""
"""
#indices
print(peliculas[1])
print(peliculas[-1])
print(animales[0:3])
print(animales[1:4])
print(animales[1:])
peliculas[0] = "El Padrino"
print(peliculas)
"""
#Añadir elemento a la lista
animales.append("Tigre")
print(animales)
animales.append("Leon")
print(animales)

peliculas.append("El padrino")
peliculas.append("Scarface")
peliculas.append("Titanic")

"""
#Recorres listas
print("*****Recorrer lista con bucle for*****")
for i in range(0, len(animales)):
	print(animales[i])

nueva_pelicula = ""
while nueva_pelicula != "parar":
	nueva_pelicula = input("Introduce una pelicula: ")	
	if nueva_pelicula != "parar":
		peliculas.append(nueva_pelicula)

else:
	#Sacamos de la lista la última películas agregada
	peliculas.pop()

print("\n")
for pelicula in peliculas:
	print(f"{peliculas.index(pelicula)+1}.-{pelicula} ")
"""

#Listas multidimensionales
print("\n*****Listado de contactos*****")

contactos = [
	[
		'Carlos',
		'calors@gmail.com',
		'735125459'
	],
	[
		'Grecia',
		'grecia@gmail.com',
		'736548962'
	],
	[
		'Diana',
		'diana@gmail.com',
		'735698522'
	]
]
print(contactos)
#Acceder al numero de telefono de la lista contactos 
print(contactos[1][2])

#Recorrer la lista multidimensional con for
print("*****Contactos*****")

for contacto in contactos:
	print(contacto)
print("\n")
print("*****For anidado*****")
for contacto in contactos:
	for elemento in contacto:
		print(elemento)
	print("\n")