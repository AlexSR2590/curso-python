"""
Diccionario es un tipo de dato que almacena un conjunto de datos.
en formato clave -> valor.
Es parecido a un array asociativo o un objeto json.
"""
personas = {
	"nombre": "Alexis",
	"apellidos": "Solis",
	"correo": "alex@gmail.com"
}

print(personas)
print(type(personas))
print(personas["apellidos"])
#Lista con diccionarios
print("\n*****Listas con diccionarios*****")

contactos = [
	{
		'nombre': 'Alexis',
		'email': 'alex@gmail.com'
	},
	{
		'nombre': 'Carlos',
		'email': 'carlos@gmail.com'
	},
	{
		'nombre': 'Selene',
		'email': 'selene@gmail.com'
	},
	{
		'nombre': 'Andrea',
		'email': 'andrea@gmail.com'
	}
]
print(contactos[2]['nombre'])
print("\n*****Cambiando valor a propiedad*****")
contactos[2]['nombre'] ="Anahi"
print(contactos[2]['nombre'])
print("_____________________________")
print("\n*****Listado de contactos*****")
for i in contactos:
	print(f"Nombre de contacto: {i['nombre']}")
	print(f"Email de contacto: {i['email']}")
	print("---------------------------")