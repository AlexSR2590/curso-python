from tkinter import *
import os.path

ventana = Tk()
ventana.title("Texto en ventana")
ruta_icono = os.path.abspath('./imagenes/logo.ico')
ruta_icono_alt = os.path.abspath('./21-tkinter/imagenes/logo.ico')

#Para cargar la ventana y el icono desde cmd o visual studio
if not os.path.isfile(ruta_icono): #Comprobando si no existe el archivo
	ruta_icono = os.path.abspath(ruta_icono_alt)

ventana.geometry("700x500")
ventana.iconbitmap(ruta_icono) #Añadiendo icono a la ventana

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
	fg="white",
	bg="black",
	padx=50,
	pady=20,
	font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Master en Python")
texto.config(
	height=3,
	bg="red",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="spider"
)
texto.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
	return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

nombre = input("Escribe tu nombre: ")
apellidos = input("Escribe tus apellidos: ")
pais = input("De que país eres: ")

texto = Label(ventana, text=pruebas(pais = pais, nombre=nombre, apellidos= apellidos))
texto.config(
	height=3,
	bg="green",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="circle"
)
texto.pack(anchor=NW)


ventana.mainloop()