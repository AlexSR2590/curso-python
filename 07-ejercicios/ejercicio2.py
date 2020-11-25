"""
	Crear un script que muestre los numero pares
	del 1 al 120
"""

for i in range(1,121):
	if i % 2 == 0 :
		print(f"Número par: {i}")
	else:
		print(f"Número impar: {i}")