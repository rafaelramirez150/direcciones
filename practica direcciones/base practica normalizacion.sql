create database direcciones;
use direcciones;

create table estado(
id_estado int primary key,
descripcion varchar(50)
);

drop table estado;

create table calle(
id_calle int primary key,
descripcion varchar(50)
);

drop table calle;

create table municipio(
id_municipio int primary key,
descripcion varchar(50),
foreign key (id_municipio)
	references estado(id_estado)on update cascade on delete cascade
);

drop table municipio;

create table colonia(
id_colonia int primary key,
descripcion varchar (100),
cp int,
foreign key (id_colonia)
	references municipio (id_municipio)on update cascade on delete cascade
);

drop table colonia;

create table persona(
id_persona int primary key,
nombre varchar(30),
num_calle int,
telefono varchar (12),
id_estado int,
id_municipio int,
id_colonia int,
id_calle int,
foreign key (id_estado)
	references estado (id_estado) on update cascade on delete cascade,
foreign key (id_municipio)
	references municipio (id_municipio) on update cascade on delete cascade,
foreign key (id_colonia)
	references colonia (id_colonia) on update cascade on delete cascade,
foreign key (id_calle)
	references calle (id_calle) on update cascade on delete cascade
);

drop table persona;

insert into estado(id_estado,descripcion) values(1,"Estado de México");
insert into estado(id_estado,descripcion) values(2,"Tlaxcala");
insert into estado(id_estado,descripcion) values(3,"Ciudad de México");
insert into estado(id_estado,descripcion) values(4,"Sonora");
insert into estado(id_estado,descripcion) values(5,"San Luis Potosí");

SELECT * FROM estado;

insert into calle(id_calle,descripcion) values(1,"Xola");
insert into calle(id_calle,descripcion) values(2,"Juan González");
insert into calle(id_calle,descripcion) values(3,"San Andrés");
insert into calle(id_calle,descripcion) values(4,"San Pablo");
insert into calle(id_calle,descripcion) values(5,"Loma");

SELECT * FROM calle;

insert into municipio(id_municipio,descripcion) values(1,"Municipio 1");
insert into municipio(id_municipio,descripcion) values(2,"Municipio 2");
insert into municipio(id_municipio,descripcion) values(3,"Municipio 3");
insert into municipio(id_municipio,descripcion) values(4,"Municipio 4");
insert into municipio(id_municipio,descripcion) values(5,"Municipio 5");

SELECT * FROM municipio;

insert into colonia(id_colonia,descripcion,cp) values(1,"El Sapo",1245);
insert into colonia(id_colonia,descripcion,cp) values(2,"San Lorenzo",23456);
insert into colonia(id_colonia,descripcion,cp) values(3,"San Luis",34567);
insert into colonia(id_colonia,descripcion,cp) values(4,"El Salto",45678);
insert into colonia(id_colonia,descripcion,cp) values(5,"Romita",56789);

SELECT * FROM colonia;

insert into persona(id_persona,nombre,num_calle,telefono,id_estado,id_municipio,id_colonia,id_calle)
	values(1,"Juan",229,5512674516,1,1,1,1);
insert into persona(id_persona,nombre,num_calle,telefono,id_estado,id_municipio,id_colonia,id_calle)
	values(2,"Pedro",116,5579203557,2,2,2,2);
insert into persona(id_persona,nombre,num_calle,telefono,id_estado,id_municipio,id_colonia,id_calle)
	values(3,"Pablo",118,5569781244,3,3,3,3);
insert into persona(id_persona,nombre,num_calle,telefono,id_estado,id_municipio,id_colonia,id_calle)
	values(4,"Ernesto",117,5569742186,4,4,4,4);
insert into persona(id_persona,nombre,num_calle,telefono,id_estado,id_municipio,id_colonia,id_calle)
	values(5,"Octavio",17,5522336699,5,5,5,5);
    
SELECT * FROM persona;

drop database direcciones;

DELETE FROM `direcciones`.`persona` WHERE (`id_persona` = '5');