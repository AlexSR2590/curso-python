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

#Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)#Para posicionar elementos dentro de la ventana
#campo_texto.pack(side=LEFT, anchor=W)

ventana.mainloop()