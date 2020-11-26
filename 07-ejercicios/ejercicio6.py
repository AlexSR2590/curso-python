"""
Hacer un programa que muestre todas las
tablas de multiplicar del 1 al 10
"""
print("*****Tablas de multiplicar*****")

contador = 1 
rango = int(input("Hata que numero quieres las tablas de multiplicar?: "))

for i in range (rango):
	#if contador <= rango :
		print('\n'+f"Tabla del {contador}")
		for i in range(1,11):		
			print(f"{contador} X {i}={contador * i}")
		contador += 1