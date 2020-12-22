import usuarios.usuario as modelo
import notas.acciones as acciones

class Acciones:
	
	def registro(self):
		print("\nOk, Vamos a registrarte en el sistema!!")
		nombre = input("¿Cual es tu nombre?: ")
		apellidos = input("¿Cuales son tus apellidos?: ")
		email = input("Escribe tu email: ")
		password = input("Escribe tu contraseña: ")

		usuario = modelo.Usuario(nombre, apellidos, email, password)
		registro = usuario.registrar()

		if registro[0] >= 1:
			print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email} ")
		else:
			print("\nNo te has registrado correctamente!!!")
	
	def login(self):
		print("\nOK, Identificate en el sistema!! ")
		try:
			email = input("Introduce tu correo: ")
			password = input("Introduce tu contraseña: ")
		
			usuario = modelo.Usuario('', '', email, password)
			login = usuario.identificar()

			if email == login[3]:
				print(f"\nBinevenido {login[1]} te has logeado en el sistema en la fecha: {login[5]}")
				self.proximasAcciones(login)

		except Exception as e:
			#print(type(e))
			print(type(e).__name__)
			print("Error...Datos incorrectos!!!")
	
	def proximasAcciones(self, usuario):
		print("""
		Acciones disponibles: 
		- Crear nota (crear)
		- Mostrar tus notas (mostrar)
		- Eliminar notas (eliminar)
		- Salir (salir)
		""")

		accion = input("¿Qué desear hacer?: ")

		hazEl = acciones.Acciones()

		if accion == "crear":
			hazEl.crear(usuario)
			self.proximasAcciones(usuario)

		elif accion == "mostrar":
			hazEl.mostrar(usuario)
			self.proximasAcciones(usuario)
		
		elif accion == "eliminar":
			hazEl.borrar(usuario)
			self.proximasAcciones(usuario)
		
		elif accion == "salir":
			print(f"Hasta pronto {usuario[1]}")
			exit()
		