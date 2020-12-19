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
cursor = database.cursor()

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

cursor.execute("show tables")

for table in cursor:
	print(table)