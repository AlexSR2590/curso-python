"""
Capturar excepciones y manejar errores en código
suceptible a errores
"""
try:
	nombre = input("Escribe tu nombre: ")
	if len(nombre) >1:
		nombre_usuario = f"El nombre es {nombre}"
	print(nombre_usuario)
except:
	print("Ocurrió un error, introduce el nombre")
else:
	print("Todo funcionó correctamente!!!")
finally:
	print("Fin de la iteración")

#Manejo de errores al buscar número en una lista

numeros = [1, 3, 5, 4, 10, 38, 2]

print("*****Busqueda de número en lista*****")
try:
	buscar = int(input("Introduce el número a buscar: "))

	comprobar = isinstance(buscar, int)
	while not comprobar or buscar <= 0:
		buscar = int(input("Introduce el número a buscar: "))
	else:
		print(f"Has introducido el número {buscar}")

	print(f"Buscar en la lista el número {buscar}")

	search = numeros.index(buscar)
	print(f"El número buscado existe en la lista en el índice {search}")	
except:
	print("El número no existe en la lista..")
finally:
	print("Busqueda finalizada")

#Manejo de multiples excepciones
try:
	numero = int(input("Dame un número para elevar el numero al cuadrado: "))
	print(f"El cuadrado del {numero} es {numero * numero}")
except TypeError:
	print("Debes convertir tu cadena a entero en el código")
#except ValueError:
#	print("Introduce un número correcto!!")
except Exception as e:
	print(type(e))
	print("Ha ocurrido un erro: ", type(e).__name__)