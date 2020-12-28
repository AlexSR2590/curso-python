from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Imagenes en tkinter").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/dios.jpg')

render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()