from tkinter import *
import os.path

ventana = Tk()
ventana.title("Posiciones")
ruta_icono = os.path.abspath('./imagenes/contenedor.ico')
ruta_icono_alt = os.path.abspath('./21-tkinter/imagenes/contenedor.ico')

if not os.path.isfile(ruta_icono):
	ruta_icono = os.path.abspath(ruta_icono_alt)

#ventana.geometry("700x500")
ventana.iconbitmap(ruta_icono)

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
	fg="white",
	bg="black",
	padx=50,
	pady=20,
	font=("Consolas", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text="Texto 2")
texto.config(
	height=3,
	bg="green",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="circle"
)
texto.pack(side=TOP, fill=X ,expand=YES)

texto = Label(ventana, text="texto 3")
texto.config(
	height=3,
	bg="red",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="circle"
)
texto.pack(side= LEFT, fill=X, expand=YES
)

texto = Label(ventana, text="texto 4")
texto.config(
	height=3,
	bg="orange",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="circle"
)
texto.pack(side= LEFT, fill=X, expand= YES)

texto = Label(ventana, text="texto 5")
texto.config(
	height= 3,
	bg="blue",
	font=("Arial", 18),
	padx=10,
	pady=20,
	cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()