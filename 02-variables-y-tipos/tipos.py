nada = None
cadena = "Este es un curso de python"
entero = 99
flotante = 4.5
booleano = True
booleano2 = False
lista = [10, 20, 30, 40, 50]
listaString = [44, "treinta", 40, "cincuenta"]
diccionario = {
	"nombre": "Alexis A.",
	"Edad": 30,
	"curso": "Master en python"
}
rango = range(9)
dato_byte = b"Probando"

#El tipo de datos Tupla, es una lista que no cambia sus valores
tuplaNoCambia = ("Curso", "de", "python")


# print(dato_byte)

#mostrar el tipo de dato
print(type(dato_byte))

#Convertir un tipo de dato a otro

texto = "Soy un texto"
numero = 123
# Error al concatenar variables string con otro tipo de dato
# print(texto + " " + numero)

#Convertir tipo de dato
numero = str(123)
print(type(numero))
print(texto + " " + numero)

numero = int(125)
print(type(numero))

numero = float(30)
print(type(numero))
print(numero)