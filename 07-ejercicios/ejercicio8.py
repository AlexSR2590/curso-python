"""
Hacer un programa donde saque el porcentaje
de un numero dado por el usuario
"""
numero = int(input("introduce número: "))
porciento = int(input("Introduce el porcentaje %: "))

#multi = numero * porciento
#porcentaje = multi / 100

multi = (numero * (porciento / 100))
print(f"El {porciento}% de {numero} es: {multi}")
