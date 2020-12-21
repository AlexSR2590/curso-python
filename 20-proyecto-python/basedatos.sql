CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios (
id int(25) auto_increment not null,
nombre varchar(100),
apellidos varchar(255),
email varchar(255) not null,
password varchar(255)not null,
fecha date not null,
constraint pk_usuarios primary key(id),
constraint uq_email unique(email)
)ENGINE=InnoDB;

CREATE TABLE notas(
id int(25) auto_increment not null,
usuario_id int(25) not null,
titulo varchar(255) not null,
descripcion mediumtext,
fecha date not null,
constraint pk_notas primary key(id),
constraint fk_nota_usuario foreign key(usuario_id) references usuarios(id)
)ENGINE=InnoDB;