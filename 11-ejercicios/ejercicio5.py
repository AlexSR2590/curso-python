"""
Crear una lista con el contenido de la sig tabla:
accion  aventura  deportes
GTA    	Assins	  FIFA 21
COD     Crash     PRO 21
PUGB    POP       MOTO GP 21
Mostrar la informacion ordenada
"""
juegos = [
	{
		'categoria': 'Accion',
		'juegos': ['GTA', 'COD', 'PUGB']
	},
	{
		'categoria': 'Aventura',
		'juegos': ['Assins', 'Crash', 'POP']
	},
	{
		'categoria': 'Deportes',
		'juegos': ['FIFA 21', 'PRO 21', 'MOTO GP 21']
	}
]

for i in juegos:
	print(f"{i['categoria']}: {i['juegos']}")