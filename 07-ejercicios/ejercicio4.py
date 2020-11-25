"""
Pedirle dos numeros al usuario y hacer
las operaciones basicas de una calculadora
"""
print("*****Calculadora*****")
numero1 = int(input("Dame el primer numero: "))
numero2 = int(input("Dame el segundo numero: "))
print("Elige operacion tecleando el simbolo: ")
print("sumar +")
print("multiplicar *")
print("restar -")
print("Dividir /")
operacion = input("Digite simbolo de operación: ")

if operacion == "+":
	print(f"La suma de {numero1} + {numero2} = {numero1 + numero2}")
elif operacion == "*":
	print(f"La multiplicacion de {numero1} * {numero2} = {numero1 * numero2}")
elif operacion == "-":
	print(f"La resta es de {numero1} - {numero2} = {numero1 - numero2}")
elif operacion == "/":
	print(f"La división es de {numero1} / {numero2} = {numero1 / numero2}")
else:
	print("ERROR, operacion incorrecta!!")