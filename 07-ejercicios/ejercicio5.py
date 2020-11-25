"""
Hacer un programa que nos muestre todos los numero
entre dos numero que da el usuario
"""
numero1 = int(input("Dame el primer número: "))
numero2 = int(input("Dame el segundo número: "))

if numero1 <= numero2:
	for i in range(numero1 + 1, numero2):
		print(i)
else:
	print("Error, el primer número debe ser menor al segundo")
