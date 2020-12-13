def holaMundo(nombre):
	return f"Hola que tal estas, {nombre}"

def calculadora(numero1, numero2, basicas = False):
	suma = numero1 + numero2
	resta = numero1 - numero2
	multiplica = numero1 + numero2
	divide = numero1 / numero2

	cadena = ""
	cadena += "Suma: " + str(suma)
	cadena += "\n"
	cadena += "Resta: " + str(resta)
	cadena += "\n"
	cadena += "Multiplicación: " + str(multiplica)
	cadena += "\n"
	cadena += "División: " + str(divide)

	if basicas == True:
		cadena = ""
		cadena += "Suma: " + str(suma)
		cadena += "\n"
		cadena += "Resta: " + str(resta)

	return cadena