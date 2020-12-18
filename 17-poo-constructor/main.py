from coche import Coche

carro = Coche("Azul", "MAZDA", "X3", 280, 215, 5)
print(carro.getInfoCoche())
print("--------------------------\n")
carro2 = Coche("Rojo", "NISSAN", "Versa", 180, 200, 4)
print(carro2.getInfoCoche())
print("--------------------------\n")
carro3 = Coche("Gris", "Mercedes", "ClaseA", 350, 380, 5)
print(carro3.getInfoCoche())

#Detectar el tipado del objeto
#carro3 = "Aleatorio"
if type(carro3) == Coche:
	print("Es un obajeto tipo Coche")
else:
	print("No es un objeto tipo Coche")

#Visibilidad (publicos y privados)

print(carro.soy_publico)
print(carro.getPrivado())