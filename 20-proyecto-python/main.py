"""
Proyecto Python MySQL:
- Abrir aistente
- Login o registro
- Si elegimos registro, creará un usuario en la base de datos
- Si elegimos login, identificará al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas
"""
#    carpeta         archivo
from usuarios import acciones

print("""
Acciones disponible:
	- registro
	- login
""")

hazEl = acciones.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion== "registro":
	hazEl.registro()

elif accion =="login":
	hazEl.login()

else:
	print("\nError... Opcion no valida!!!")