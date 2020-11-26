print("*****Funciones*****")

"""
***declarando una función***
def nombreFuncion(parametros):
	print("Spy una función")
"""
#Ejemplo 1
print("*****Ejemeplo 1*****")

def muestraNombre():
	print("Alex")
	print("Nestor")
	print("Carlos")
	print("Grecia")

#Llamando función
muestraNombre()
print("______________________\n")

#Ejemplo 2
print("*****Ejemeplo 2*****")
"""
def mostrarNombre(nombre, edad):
	nombre_usuario = input("Escribe tu nombre: ")
	edad_usuario = int(input("Cúal es tu edad?: "))
	print(f"Hola!! {nombre_usuario}")
	if edad_usuario < 18:
		print("Eres menor de edad!!")
	else:
		print("Eres mayor de edad!!")

nombre = " "
edad = 0
mostrarNombre(nombre, edad)
#mostrarNombre(nombre, edad)
#mostrarNombre(nombre, edad)
"""
"""
def mostrarNombre():
	nombre = input("Escribe tu nombre: ")
	print(f"Hola!! {nombre}")

mostrarNombre()

"""
print("______________________\n")

#Ejemplo 3
#Tablas de multiplicar con funciones
print("*****Ejemeplo 3*****")

numero = int(input("De qué número quieres la tabla de multiplicación?: "))

def tablaMultiplicacion(numero):
	print(f"Tabla del número {numero}")
	for i in range(1,11):
		print(f"{numero} X {i} = {numero * i}")
	else:
		print("Tabla finalizada!!")

tablaMultiplicacion(numero)

#Ejemplo 3.1
#Sacar las tablas de multiplicar del 1 al 10 utilizando la función

for i in range(1,5):
	tablaMultiplicacion(i)
	print("\n")

print("______________________\n")

#Ejemplo 4
#Parametros opcionales
"""
Cuando se quiere que un parametro sea opcional
se debe asignarle un valor por defecto en los
parametros de la función
"""
print("*****Ejemeplo 4*****")

def getEmpleado(nombre, id = False):
	print("Empleado")
	print(f"Nombre: {nombre}")
	print(f"Identicador empleado: {id}")

getEmpleado("Alexis Arturo", 1234)
getEmpleado("Carlos")

print("______________________\n")

#Ejemplo 5
#Parametros opcionales y retorno de valor de una función
print("*****Ejemplo 5*****")

def saludame(nombre):
	saludo = f"Hola!! Saludos {nombre}"
	return saludo

print(saludame("Alexis"))

print("______________________\n")

#Ejemplo 6
#Ejemplo de calculadora
print("*****Ejemplo 6*****")

print("\nSin parametro True")

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

print(calculadora(5, 5))
print("\nCon parametro True")
print(calculadora(10, 5, True))

print("______________________\n")

#Ejemplo 7
#Función dentro de otra función
print("*****Ejemplo 7*****")

def getNombre(nombre):
	texto = f"El nobre es: {nombre}"
	return texto

def getApellidos(apellidos):
	texto = f"Los apellidos son: {apellidos}"
	return texto
"""
print(getNombre("Alexis"))
print(getApellidos("Solis R."))
"""
def nombreCompleto(nombre, apellidos):
	texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
	return texto

print(nombreCompleto("Alexis", "Solis R."))

print("______________________\n")

#Ejemplo 8
#Función Lambda (anonimas)
print("*****Ejemplo 8*****")

año_actual = lambda year: f"El año es {year + 1}"
año = int(input("Dime el año: "))
print(año_actual(año))