#Condicional IF
#Ejemplo 1
print("-----Ejemplo 1------")

#color = input("Adivina mi color favorito: ")
color = "negro"
if color == "negro":
	print(f"El color {color}, es mi color favorito")
else:
	print(f'El color "{color}" no es mi color favorito')

print("____________________________________")

#Operadores de comparación
"""
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""

#Ejemplo 2
print("-----Ejemplo 2------")

#year = int(input("¿Cúal es el año actual?: "))

year = 2020
if year >= 2021:
	print("Estamos de 2021 en adelante!!")
else:
	print("Es un año anterior al 2021")

print("____________________________________")

#Ejemplo 3
print("-----Ejemplo 3------")
"""
nombre = input("¿Cúal es tu nombre?: ")
ciudad = input("¿En que ciudad vives?: ")
continente = input("¿Cúal es tu continente?: ")
edad = int(input("Introduce tu edad: "))
"""
nombre = "Arturo"
ciudad = "Mexico"
continente = "Americano"
edad = 27
mayorida_edad = 18

if edad >= mayorida_edad:
	print(f"{nombre} con {edad} años, eres mayor de edad")

	if continente != "Americano":
		print(f"{nombre} no eres Americano!!")
	else:
		print(f"Eres {continente} de la ciudad {ciudad}")

else: 
	print(f"{nombre} eres menor de edad!!")

print("____________________________________")

#Ejemplo 4
print("-----Ejemplo 4------")

#dia = int(input("Introduce el numero del día de la semana: "))

"""
if dia == 1:
	print("Día Lunes")
else:
	if dia == 2:
		print("Día Martes")
	else:
		if dia == 3:
			print("Día Miercoles")
		else:
			if dia == 4:
				print("Día Jueves")
			else:
				if dia == 5:
					print("Día Viernes")
				else:
					if dia == 6:
						print("Día Sabado")
					else:
						if dia == 7:
							print("Día Domingo")
						else:
							print("Error!! Numero de día invalido")
"""
dia = 1
if dia == 1:
	print("Día Lunes")
elif dia == 2:
	print("Día Martes")
elif dia == 3:
	print("Día Miercoles")
elif dia == 4:
	print("Día Jueves")
elif dia == 5:
	print("Día Viernes")
elif dia == 6:
	print("Día Sabado")
elif dia == 7:
	print("Día Domingo")
else:
	print("Error!! Numero de día invalido")

print("____________________________________")

#Ejemplo 5
print("-----Ejemplo 5------")
edad_minima = 18
edad_maxima = 65
#edad_persona = int(input("¿Cúal es tu edad?: "))
edad_persona = 25

if edad_persona >= edad_minima and edad_persona <= edad_maxima:
	print("Tienes edad para trabajar!!")
else:
	print("No tienes edad para trabajar!!")

print("____________________________________")

#Ejemplo 6
print("-----Ejemplo 6------")

#pais = input("¿De qué país eres?: ")
pais ="Alemania"

if pais == "Mexico" or pais == "España" or pais =="Colombia":
	print(f"{pais} es un país de habla hispana")
else:
	print(f"{pais} no es un país de habla hispana")

print("____________________________________")

#Ejemplo 7
print("-----Ejemplo 7------")

#pais = input("¿De qué país eres?: ")
pais ="Mexico"

if not (pais == "Mexico" or pais == "España" or pais =="Colombia"):
	print(f"{pais} no es un país de habla hispana")
else:
	print(f"{pais} es un país de habla hispana")

print("____________________________________")

#Ejemplo 8
print("-----Ejemplo 8------")

#pais = input("¿De qué país eres?: ")
pais ="Noruega"

if pais != "Mexico" and pais != "España" and pais !="Colombia":
	print(f"{pais} no es un país de habla hispana")
else:
	print(f"{pais} es un país de habla hispana")
