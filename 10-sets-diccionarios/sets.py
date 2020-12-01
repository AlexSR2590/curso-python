"""
SET es un tipo de dato, para tener una coleccion de valores, pero no tiene
ni indice ni orden
"""
personas = {
	"Luis",
	"Alejandro",
	"Anaid",
	"Grecia",
	"Alexis"
}
print(personas)
print(type(personas))

#Agregar un elemento al set
personas.add("Arturo")

#Eliminar un elemento del set
personas.remove("Alexis")
print("\n")
print(personas)

