#Excepsiones personalizadaso lanzar excepción
try:
	nombre = input("Escribe tu nombre: ")
	edad = int(input("Introduce tu edad: "))

	if edad < 5 or edad > 110:
		raise ValueError("La edad introducida no es real")
	elif len(nombre) <=1:
		raise ValueError("El nombre no esta completo")
	else:
		print(f"Bienvenido al master en Python {nombre}")
except ValueError:
	print("Introduce los datos correctamente")
except Exception as e:
	print("Existe un error: ",e)