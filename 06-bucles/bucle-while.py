print("*****Bucle While*****")

contador = 1

while contador <= 10:
	print(f"Iteracíon: {contador}")
	contador += 1

print("__________________________")

print("*****Ejemplo 2*****")
contador2 = 1
muestra = str(0)
while contador2 <= 100:
	muestra = muestra + ", " + str(contador2)
	contador2 += 1

print(muestra)

print("__________________________")

print("*****Ejemplo 3*****")
#Tabla de multiplicar con el while

numero = int(input("Dame numero para multiplicar: "))
i = 1

while i <= 10:
	print(f"{numero} X {i} = {numero * i}")
	i += 1
else: 
	print("Tabla terminada!!")	