nombre = "Alexis"
#funciones generales
print(nombre)
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
	print("Esa variable es un string")
else:
	print("No es un string")

if not isinstance(nombre, float):
	print("La variable no es un número con decimales")

#Limpiar espacios
frase = "      El contenido tiene espacios"
print(frase)
print("\nUsando la funcon strip() para quitar espacios")
print(frase.strip())

#Eliminar variables
year = 2020
print(year)
del year
#print(year)

#Comprobar variables vacias
texto = " ff "
if len(texto) <=0:
	print("La variables esta vacia")
else:
	print("La variable tiene contenido", len(texto))

#Encontrar caracteres dentro de un string
frase = "Lo que yo quiero saber es..."
print(frase)
print(frase.find("quiero"))

#Reemplazar palabras dentro de un string
nueva_frase = frase.replace("quiero", "necesito")
print(nueva_frase)

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())
