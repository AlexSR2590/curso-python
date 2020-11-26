"""
Recomendaciones
1.- La declaración de las funciones deben de ir
	el inicio del fichero
2.- Las no es recomendable tener prints dentro de las funcioes
	es mejor que siempre devuelvan un dato
"""
#def miFuncion():
#	print("Esta es mi función")

"""
#Es posible acceder a las variables globales
includo cuando las funciones son declaradas primero
Solo es necesario que las variables esten declaradas antes 
de llamar la funcion
"""
def miFuncion(nombre):
	return "Ésta es mi función 1 " + nombre

#def miFuncion2():
#	print("Eta es mi función 2")

def miFuncion2(apellidos):
	return "Ésta es mi función 2 " + apellidos


nombre = "Alexis"
apellidos = "Solis R."

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(miFuncion(nombre))
print(miFuncion2(apellidos))