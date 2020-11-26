"""
Hacer un programa que pida las calificaciones
de 15 alumnos y que nos muestre cuantos han pasado
y cuantos reprobaron
"""
aprobados = 0
reprobados = 0
contador = 0
numero_alumnos = int(input("Cúantos alumnos tienes: "))

while contador < numero_alumnos:
	calificacion = float(input(f"Escribe la calificación para el alumno {contador}: "))

	if calificacion >= 6:
		aprobados += 1
	else:
		reprobados += 1

	contador += 1

print("*****Alumnos aprobados*****")
print(aprobados)
print("_______________________________")	
print("*****Alumnos reprobados*****")
print(reprobados)
