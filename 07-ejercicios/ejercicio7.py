"""
Hacer un programa que nos muestre todos los números
impares entre dos numero que de el usuario
"""
numero1 = int(input("Dame el primer número: "))
numero2 = int(input("Dame el segundo número: "))

if numero1 < numero2 and numero1 >=0 and numero2 >=0:
	# mostrar numeros impares entre los numero dados
	for i in range(numero1, numero2 + 1):
		residuo = i % 2
		if residuo != 0:
			print(f"Número impar: {i}")
		else:
			print(f"Número par: {i}")
else:
	print("Error!!, El primer número debe ser menor al segundo número")
