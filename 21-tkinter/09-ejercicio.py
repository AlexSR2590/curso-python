from tkinter import * 
from tkinter import messagebox as MessageBox
"""
Calculadora:
- Dos campos de texto
- 4 Botones para las operaciones
- mostrar el resultado en una alerta
"""
class Interfaz:
	def __init__(self, ventana):
		#Inicializando ventana
		self.ventana=ventana
		self.ventana.geometry("400x400")
		self.ventana.title("Calculadora")
		self.ventana.config(bd=25)
		return
	
ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)

"""
def getSuma():
	resultado.set(numero1.get() + numero2.get())

def getResta():
	resultado.set(numero1.get() - numero2.get())

def getMultiplicacion():
	resultado.set(numero1.get() * numero2.get())

def getDivision():
	resultado.set(numero1.get() / numero2.get())

numero1= IntVar()
numero2= IntVar()
resultado = IntVar()

Label(ventana_principal, text="Introduce el primer número: ").pack(anchor=NW)
Entry(ventana_principal, textvariable=numero1).pack(anchor=NW)

Label(ventana_principal, text="Introduce el segundo número: ").pack(anchor=NW)
Entry(ventana_principal, textvariable=numero2).pack(anchor=NW)

boton_sum = Button(ventana_principal, text="+", command=getSuma)
boton_sum.pack()

boton_res = Button(ventana_principal, text="-", command=getResta)
boton_res.pack()

boton_mult= Button(ventana_principal, text="x", command=getMultiplicacion)
boton_mult.pack()

boton_div = Button(ventana_principal, text="/", command=getDivision)
boton_div.pack()

Label(ventana_principal, text="Respuesta").pack(anchor=NW)
texto_recogido = Label(ventana_principal, textvariable=resultado)
texto_recogido.pack(anchor=NW)
"""

def cFloat(numero):
	try:
		result = float(numero)
	except:
		result = 0
		MessageBox.showerror("Error", "Introduce bien el número")
	return result
	
def sumar():
	resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
	mostrarResultado()

def restar():
	resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
	mostrarResultado()

def multiplicar():
	resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
	mostrarResultado()

def dividir():
	resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
	mostrarResultado()

def mostrarResultado():
	MessageBox.showinfo("Resultado", f"{resultado.get()}")
	numero1.set("")
	numero2.set("")


numero1 = StringVar()
numero2= StringVar()
resultado = StringVar()

marco = Frame(ventana_principal, width=250, height=200)
marco.config(
	padx=15,
	pady=15,
	bd=5,
	relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left")
Button(marco, text="Restar", command=restar).pack(side="left")
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left")
Button(marco, text="Dividir", command=dividir).pack(side="left")

ventana_principal.mainloop()