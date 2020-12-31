from tkinter import *

ventana = Tk()
ventana.title("Formulario 2 en tkinter")
ventana.geometry("400x400")

encabezado= Label(ventana, text="Formularios 2")
encabezado.config(
	padx= 15,
	pady= 15,
	fg="white",
	bg="green",
	font=("Consolas", 20)
)
encabezado.grid(row= 0, column=0, columnspan=5, sticky=W)

def mostrarProfesion():
	texto = ""

	if web.get():
		texto="Desarrollador Web"

	if movil.get():
		if web.get():
			texto += " Y Desarrollo Movil"
		else:
			texto += "Desarrollador movil"
	
	mostrar.config(
		bg="brown", 
		text=texto,
		fg="white"
	)	

#Variables para los botones check
web = IntVar()
movil = IntVar()


#Botones de check
Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0, sticky=W)

Checkbutton(
	ventana, 
	text="Desarrollo Web",
	variable=web,
	onvalue=1, #tomará el valor 1 cuando esté marcado
	offvalue=0, #tomará el valor de 0 cuando no esté marcado 
	command=mostrarProfesion
).grid(row=2, column=0, sticky=W)

Checkbutton(
	ventana, 
	text="Desarrollo movil",
	variable= movil,
	onvalue=1,
	offvalue=0,
	command=mostrarProfesion #Cuando se seleccione el check box, se llamara a la funcion mostrarProfesion()
).grid(row=3, column=0, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


#Radio buttons

def marcar():
	marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)
Label(ventana, text="¿Cuál es tu genero?").grid(row=5)

Radiobutton(
	ventana, 
	text="Masculino", 
	value="Masculino",
	variable=opcion,
	command=marcar
).grid(row=6)

Radiobutton(
	ventana, 
	text="Femenino",
	value="Femenino",
	variable= opcion, #Es la variable que se va a modificar cuando se toca el radio button
	command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

#Option Menu

def seleccionar():
	seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1")

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

select= OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)
ventana.mainloop()
