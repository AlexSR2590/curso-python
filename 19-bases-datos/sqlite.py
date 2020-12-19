#Importar modulo de base de datos
import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
titulo VARCHAR(255),
descripcion TEXT,
precio int(255)
)""")

#Guardar cambios
conexion.commit()

"""
#Insertar datos
cursor.execute("insert into productos values(null, 'segundo producto', 'descripcion del producto', 552)")
conexion.commit()
"""

#Borrar registros 
#cursor.execute("delete from productos")
#conexion.commit()

#Insertar muchos registros 
"""
productos = [
	("Laptop Dell", "Geming", 25000),
	("PC Escritorio", "Oficina", 7000),
	("Smart phone", "xiaomi", 6500),
	("Camara de video", "sport", 5000)
]

cursor.executemany("insert into productos values(null, ?, ?, ?)", productos)
conexion.commit()
"""
#Update
cursor.execute("update productos set precio = 20000 where titulo = 'Laptop Dell' ")

#Listar datos
cursor.execute("select * from productos where precio >= 7000 ")

productos = cursor.fetchall()

for producto in productos:
	print("Id: ", producto[0])
	print("Titulo: ", producto[1])
	print("Descripcion: ", producto[2])
	print("Precio: ", producto[3])
	print("\n")

cursor.execute("Select titulo from productos")
producto = cursor.fetchone()
print(producto)


#Cerrar conexión
conexion.close()


