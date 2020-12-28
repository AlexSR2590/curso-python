from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")
"""
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco= Frame(marco_padre, width=250, height=250)
marco.config(
	bg="yellow",
	bd=5,
	relief="sunken"
)
marco.pack(side=LEFT)
marco.pack_propagate(False)#Para mantener el marco del mismo tamaño
texto = input("Escribe el contenido del primer cuadro: ")
Label(marco, text=texto).pack(side=BOTTOM, anchor=CENTER)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="red",
	bd=5,
	relief="raised"
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)
texto = input("Escribe el contenido del segundo cuadro: ")
Label(marco, text=texto).pack(side=BOTTOM, anchor=CENTER)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)
#marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="orange",
	bd=5,
	relief="raised"
)
marco.pack(side=LEFT)
marco.pack_propagate(False)
texto = input("Escribe el contenido del tercer cuadro: ")
Label(marco, text=texto).pack(side=BOTTOM, anchor=CENTER)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="brown",
	bd=5,
	relief="raised"
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)
texto = input("Escribe el contenido del cuarto cuadro: ")
Label(marco, text=texto).pack(side=BOTTOM, anchor=CENTER)
"""
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco= Frame(marco_padre, width=250, height=250)
marco.config(
	bg="yellow",
	bd=5,
	relief="sunken"
)
marco.pack(side=LEFT)
marco.pack_propagate(False)#Para mantener el marco del mismo tamaño
texto = Label(marco, text="Primer cuadro")
texto.config(
	bg="red",
	fg="white",
	font=("Arial", 20)	
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="red",
	bd=5,
	relief="raised"
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)
Label(marco, text="Segundo cuadro").pack(side=BOTTOM, anchor=CENTER)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)
#marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="orange",
	bd=5,
	relief="raised"
)
marco.pack(side=LEFT)
marco.pack_propagate(False)
Label(marco, text="Tercer cuadro").pack(side=BOTTOM, anchor=CENTER)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
	bg="brown",
	bd=5,
	relief="raised"
)
marco.pack(side=RIGHT)
marco.pack_propagate(False)
Label(marco, text="Cuarto cuadro").pack(side=BOTTOM, anchor=CENTER)

ventana.mainloop()