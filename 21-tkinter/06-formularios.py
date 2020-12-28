from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

#Texto encabezado
encabezado = Label(ventana, text="Formularios con tkinter")
encabezado.config(
	fg="white",
	bg="darkgray",
	font=("Open Sans", 18),
	padx=10,
	pady=10	
)
encabezado.grid(row=0, column=0, columnspan=10, sticky=W)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

#Label para el campo nombre
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Campo de texto para nombre
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)#Para posicionar elementos dentro de la ventana
campo_texto.config(justify="left", state="normal")
#campo_texto.pack(side=LEFT, anchor=W)

#Label para apelliodos
label = Label(ventana, text="Apellidos")
label.grid(row = 2, column= 0, sticky=W, padx=5, pady=5)

#Campo texto para apellidos
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column = 1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#Label para descripción
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#Campo de texto grande para descripción
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, padx=5, pady=5)
campo_grande.config(
	width=30,
	height=5,
	font=("Arial", 12)
)

#Boton
Label(ventana).grid(row=4, column=1)#Campo de separación entre el boton y el área de texto
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
	padx=10,
	pady=10,
	bg="green",
	fg="white"
)

ventana.mainloop()