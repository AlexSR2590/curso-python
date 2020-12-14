from io import open
import pathlib
import shutil
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir dentro de un archivo
archivo.write("****Soy un texto escrito desde Python****\n")

#Cerrar archivo
archivo.close()

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()

#print(contenido)
"""
for elemento in contenido:
	print(elemento)
"""
#Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
for elemento in lista:
	lista_frase = elemento.split()
	print(lista_frase)
		#print(elemento.upper)

# Copiar archivo
#ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"
#shutil.copyfile(ruta_original, ruta_nueva)

# Mover un archivo
"""
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original, ruta_nueva)
"""
#Eliminar archivos
import os
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

#os.remove(ruta_nueva)

#Comprobar si existe
import os.path
#print(os.abspath("../"))
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
	print("El archivo exite")
else:
	print("El archivo no existe")