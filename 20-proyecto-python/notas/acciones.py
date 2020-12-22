import notas.nota as modelo

class Acciones():

	def crear(self, usuario):
		print(f"\n{usuario[1]} Vamor a crear una nueva nota!!!")
		titulo = input("\nEscribe el título de la nota: ")
		descripcion = input("Escribe la nota: ")

		nota = modelo.Nota(usuario[0], titulo, descripcion)
		guardar = nota.guardar()

		if guardar[0] >= 1:
			print(f"\nSe guardó la nota: {nota.titulo}")
		else:
			print(f"No se ha guardado la nota, lo siento {usuario[1]}")

	
	def mostrar(self, usuario):
		print(f"\nNotas de el usuario {usuario[1]} !!!\n")

		nota = modelo.Nota(usuario[0])
		notas = nota.listar()

		for nota in notas:
			print("-------------------")
			print(nota[2])
			print(nota[3])
			print(f"Fecha: {nota[4]}")
	
	def borrar(self, usuario):
		print(f"\nHola {usuario[1]} vamos a eliminar notas")
		titulo = input("Escribe el título de la nota a borrar: ")

		nota = modelo.Nota(usuario[0], titulo)
		eliminar = nota.eliminar()


		if eliminar[0] >= 1:
			print(f"\nSe eliminó la nota {nota.titulo}")
		else:
			print("No se ha borrado la nota!!!")