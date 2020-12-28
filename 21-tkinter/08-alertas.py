from tkinter import *
from tkinter import messagebox as MessageBox

def sacarAlerta():
	#MessageBox.showinfo("Alerta", "Curso Master en python")
	#MessageBox.showwarning("Alerta", "Curso Master en python")
	MessageBox.showerror("Alerta", "Curso Master en python")
	
def salir(nombre):
	resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicación?")
	if resultado != "yes":
		MessageBox.showinfo("Hasta pronto!!!", f"Adios {nombre}" )
		ventana.destroy()


ventana = Tk()
ventana.config(bd=70)

Button(ventana, text="Alerta", command=sacarAlerta).pack()
Button(ventana, text="Salir", command=lambda: salir("Carlos")).pack()



ventana.mainloop()