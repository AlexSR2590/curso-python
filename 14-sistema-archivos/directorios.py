import os
import shutil
#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
	os.mkdir("./mi_carpeta")
else:
	print("Directorio existe")

#Eliminar una carpeta
#os.rmdir("./mi_carpeta")

#Copiar una carpeta
#ruta_original = "./mi_carpeta"
#ruta_nueva = "./mi_carpeta_copiada"
#shutil.copytree(ruta_original, ruta_nueva)

#Eliminar carpeta copiada
#os.rmdir("./mi_carpeta_copiada")

print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
for fichero in contenido:
	print("Fichero: ", fichero)