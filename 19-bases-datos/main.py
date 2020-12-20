import mysql.connector

#Conexión a base de datos
database = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="master_python"
)

#Comprobando la conexión
# print(database)

#Cursor que nos permite realizar las consultas
cursor = database.cursor(buffered= True)

#Creando base de datos
cursor.execute("create database if not exists master_python")

#cursor.execute("show databases")
"""
for bd in cursor:
	print(bd)
"""
#Crear tablas
cursor.execute("""
create table if not exists vehiculos(
	id int(10) auto_increment not null,
	marca varchar(40) not null,
	modelo varchar(40) not null,
	precio float(10,2) not null,
	constraint pk_vehiculo primary key(id)
)
""")
#Mostrando las tablas 
"""
cursor.execute("show tables")

for table in cursor:
	print(table)
"""
#cursor.execute("insert into vehiculos values(null, 'NISSAN','370z', 500.14 )")
"""
coches = [
	('Seat', 'Leon', 350000.65),
	('Mazda', 'x5', 452200.50),
	('Ford', 'mustang 2020', 500000.30),
	('Mercedez', 'SLK', 1000000.10)
]
"""
#cursor.executemany("insert into vehiculos values(null, %s, %s, %s)", coches)
#database.commit()

cursor.execute("select * from vehiculos")

print("-----Lista de vehiculos-----")
result = cursor.fetchall()
#Mostrando la marca y el precio

print("------------------------")
for vehiculo in result:
	print(f"Marca: {vehiculo[1]} Precio: {vehiculo[3]}")

#Obtener registro de un solo coche

print("------------------------")
print("\nObtener registro de un solo coche")
cursor.execute("select * from vehiculos")
coche = cursor.fetchone()
print(coche)

#Eliminar registros de una tabla
print("------------------------")
cursor.execute("delete from vehiculos where marca = 'Seat' ")
database.commit()
print(cursor.rowcount, "borrados!!")
#Mostrando los vehiculos
cursor.execute("select * from vehiculos")
for vehiculo in cursor:
	print(vehiculo)

#Actualizar 
print("-------------------------")
cursor.execute("update vehiculos set modelo = 'Fiesta' where marca = 'Ford'")
database.commit()
cursor.execute("select * from vehiculos")
for vehiculo in cursor:
	print(vehiculo)

