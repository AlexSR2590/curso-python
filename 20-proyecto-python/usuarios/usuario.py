import usuarios.conexion as conexion 
import datetime
import hashlib #Sifrar contraseña

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

	def __init__(self, nombre, apellidos, email, password):
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email
		self.password = password
	
	def registrar(self):
		fecha = datetime.datetime.now()
		#sifrar contraseña
		cifrado = hashlib.sha256()
		cifrado.update(self.password.encode('utf8'))
		sql = "insert into usuarios values(null, %s, %s, %s, %s, %s)"
		usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha ) #tupla
		
		try:
			cursor.execute(sql, usuario)
			database.commit()
			result = [cursor.rowcount, self]
		except:
			result = [0, self]
		return result

	def identificar(self):
		#consulta para comprobar el usuario
		sql = "select * from usuarios where email = %s and password = %s"

		#Cifrando contraseña
		cifrado = hashlib.sha256()
		cifrado.update(self.password.encode('utf8'))

		#Datos para la consulta
		llave = (self.email, cifrado.hexdigest() )

		#Consulta
		cursor.execute(sql, llave)
		result = cursor.fetchone()
		return result
	#Posiblemente eliminar usuario

	#Posiblemende modificar usuario

	#Posiblemente listar usuarios