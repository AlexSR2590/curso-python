"""
Escribir un programa los cuadrados de los 
60 primeros numero naturales, usar bucle while 
y for
"""
print("*****Bucle While*****")
i = 0
while i <= 60:
	print(f"EL cuadrado de {i} es: {i * i}")
	i += 1
else:
	print("Programa terminado con bucle while!!")

print("______________________________")

print("*****Bucle For*****")

for j in range(61):
	print(f"EL cuadrado de {j} es: {j * j}")
else:
	print("Programa terminado con bucle For!!")