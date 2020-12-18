#Definiendo clase coche

class Coche:
	color = "Negro"
	marca = "NISSAN"
	modelo = "370z"
	velocidad = 350
	caballaje = 450
	plazas = 2

	soy_publico = "Propiedad publica"
	__Soy_privado = "Propiedad privada"

#Definiendo constructor
	def getPrivado(self):
		return self.__Soy_privado

	def __init__(self,color, marca, modelo, velocidad, caballaje, plazas):
		self.color = color
		self.marca = marca
		self.modelo = modelo
		self.velocidad = velocidad
		self.caballaje = caballaje
		self.plazas = plazas

#Definiendo metodos
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

	def setMarca(self, marca):
		self.marca = marca
	
	def getMarca(self):
		return self.marca
	
	def setModelos(self, modelo):
		self.modelo = modelo
	
	def getModelo(self):
		return self.modelo
	
	def setCaballaje(self, caballaje):
		self.caballaje = caballaje
	
	def getCaballaje(self):
		return self.caballaje
	
	def setPlazas(self, plazas):
		self.plazas = plazas

	def getPlazas(self):
		return self.plazas

	def getInfoCoche(self):
		info = "-----Información del coche-----"
		info += "\n Color: " + self.getColor()
		info += "\n Marca: " + self.getMarca()
		info += "\n Modelo: " + self.getModelo()
		info + "\n Velocidad: " + str(self.getVelocidad())
		info += "\n Caballaje: " + str(self.getCaballaje())
		info += "\n Plazas: " + str(self.getPlazas())
		return info