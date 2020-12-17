"""
Programación orientada a objetos
"""
#Definir clase (molde para crear más objetos de ese tipo)
class Coche:
	#Atributos o propiedades
	color = "rojo"
	marca = "Ferrari"
	modelo = "Enzo"
	velocidad = 300
	caballaje = 500
	plazas = 2

	#Metodos, son acciones que hace el objeto (funciones)
	def acelerar(self):
		self.velocidad += 1
	
	def frenar(self):
		self.velocidad -= 1
	
	def getVelocidad(self):
		return self.velocidad
	
	def setColor(self, color):
		self.color = color
	
	def getColor(self):
		return self.color
	
	def setModelo(self, modelo):
		self.modelo = modelo
	
	def getModelo(self):
		return self.modelo

	#Fin de definición de la clase

coche = Coche()
print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Nueva velocidad: {coche.getVelocidad()} Km/h")

coche.frenar()
coche.frenar()
coche.frenar()
coche.frenar()
print(f"Disminuir velocidad: {coche.getVelocidad()} Km/h")

print(f"Modelo del auto: {coche.getModelo()} ")

print("*****Cambiando color del auto*****\n")

print(f"Color actual del auto: {coche.getColor()}")
#nuevo_color = input("Que color quieres el auto: ")
nuevo_color = "negro"
coche.setColor(nuevo_color)
print(f"Nuevo color del auto: {coche.getColor()}")

#creando mas obejtos
print("\n***Creaando camioneta***")
camioneta = Coche()
print(f"Camioneta: {camioneta.getColor()}")
camioneta.setColor("Blanca")
camioneta.setModelo("Frontier")
print(f"Modelo de la camioneta: {camioneta.getModelo()}")