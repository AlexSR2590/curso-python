print("********Bucle For********")

contador = 0
resultado = 0
for contador in range(0,10):
	print("Numero de iteración: "+ str(contador))
	resultado += contador
	print("Suma del contador " + str(resultado))

print("-------EJEMPLO MULTIPLICAR-------")

numero1 = int(input("Dame un numero: "))

if numero1 >= 1: 
	for i in range(1,11):
		if numero1 >= 20:
			print("No acepto número del 20 en adelante!!")
			break
		else:
			resultado = numero1 * i
			print(f"{numero1} X {i} = {resultado}")
	else:
		print("Tabla finalizada!!")
else:
	print("Error!! el numero tiene que ser mayor a 0")