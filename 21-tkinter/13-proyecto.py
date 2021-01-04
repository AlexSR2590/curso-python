"""
Crear un programa que tenga
- Ventana (hecho)
- Tamaño fijo (hecho)
- No redimensionable (hecho)
- Un menu (Inicio, Añadir, Información, salir)(Hecho)
- Opcion de salir (Hecho)
- Diferentes pantallas (Hecho)
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home

"""
from tkinter import *

#Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto tkinter - Master en Python")
ventana.resizable(0, 0)#Para dejar el tamaño de la ventana fija

#Pantallas
def home():
	home_label.config(
		fg="white",
		bg="black",
		font=("Arial", 20),
		padx=218,
		pady=20
	)
	home_label.grid(row=0, column=0)

	#Ocultar otras pantallas
	add_label.grid_remove()
	info_label.grid_remove()
	data_label.grid_remove()

	return True

def add():
	#Encabezado
	add_label.config(
		fg="white",
		bg="black",
		font=("Arial", 20),
		padx=160,
		pady=20
	)
	add_label.grid(row=0, column=0, columnspan=4, sticky=NW)

	#Campos del formulario
	add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
	add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

	add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
	add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

	add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
	add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

	#Ocultando otras pantallas
	home_label.grid_remove()
	info_label.grid_remove()
	data_label.grid_remove()


	return True

def info():
	info_label.config(
		fg="white",
		bg="black",
		font=("Arial", 20),
		padx=180,
		pady=20
	)
	info_label.grid(row=0, column=0)	
	data_label.grid(row=1, column=0)
	
	#Ocultando otras pantallas
	home_label.grid_remove()
	add_label.grid_remove()
	
	return True

#Variables importantes
name_data= StringVar()
price_data = StringVar()

#Definir campo de pantalla Inicio
home_label = Label(ventana, text="Inicio")


#Definir campo de pantalla Añador
add_label = Label(ventana, text="Añadir producto")

#Campos del formulario
add_name_label = Label(ventana, text="Nombre: ")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio: ")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripción: ")
add_description_entry = Text(ventana)

#Definir campo de pantalla Información
info_label = Label(ventana, text="Información")


#Definir campo de pantalla dato
data_label= Label(ventana, text="Año 2021- Master en Python")


#Cargar pantalla inicio
home()

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargando menu
ventana.config(menu=menu_superior)

#Cargar ventana
ventana.mainloop()