"""
Programa que compruebe si una variable esta vacia
y si lo está, asignarle un valor con texto en minusculas
y mostrarlas en mayusculas
"""
variable = input("Introduce un texto: ")

while len(variable.strip())<= 0:
	if len(variable.strip()) <= 0:
		variable = input("La variables está vacia, introduce un texto: ")
		print("Valor asignado: " + variable.lower())
else:
	print("Valor mostrado: " + variable.upper())

