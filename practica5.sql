#practica 5
#Jonathan Mendez Martinez
#23270063
#10/02/25
-- source C:\Users\jonathan\Documents\S5A\admin basedat\practica5.sql
-- Tabla de usuarios
DROP DATABASE IF EXISTS practica05_usuarios;
CREATE DATABASE practica05_usuarios;
USE practica05_usuarios;


CREATE TABLE lineainv(
	clavein CHAR(10) PRIMARY KEY,
	nombre VARCHAR(250)
 );

CREATE TABLE profesor(
	idprofesor INT AUTO_INCREMENT PRIMARY KEY,
	nombreProf VARCHAR(200));

CREATE TABLE tipoproyecto(
	tipo char(10) PRIMARY KEY, 
	nombre VARCHAR(150));

CREATE TABLE proyecto(
	clave CHAR(10) PRIMARY KEY,
	nombre VARCHAR(250), clavein CHAR(10), 
	tipo CHAR(10),
    CONSTRAINT corresponde FOREIGN KEY (clavein) REFERENCES lineainv(clavein),
    CONSTRAINT asignado FOREIGN KEY (tipo) REFERENCES tipoproyecto(tipo)
);

CREATE TABLE alumno(
	nocontrol CHAR(10) PRIMARY KEY,
	nombre VARCHAR(150), 
	clave CHAR(10),
    CONSTRAINT elige FOREIGN KEY (clave) REFERENCES proyecto(clave)
);

CREATE TABLE profesorproy(
	idprofesor INT, clave CHAR(10),
	calificacion FLOAT, rol VARCHAR(45),
    CONSTRAINT asesora FOREIGN KEY (idprofesor) REFERENCES profesor(idprofesor),
    CONSTRAINT asigna FOREIGN KEY (clave) REFERENCES proyecto(clave)
);
    
CREATE TABLE datos(
	clave char(8), 
	proyecto varchar(150),
	linea char(10),
	tipo char(5),  
	nocontrol char(10), 
	nombre_alumno varchar(150),
	nombreProf varchar(150),
	revisor1 varchar(150), 
	revisor2 varchar(150)
);
-- *******************************+

CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo ENUM('admin', 'profesor', 'alumno') NOT NULL -- ROLES
);


CREATE TABLE Permisos (
    id_permiso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_permiso ENUM('lectura', 'escritura', 'actualizacion', 'eliminacion') NOT NULL -- asignacion de Permisos
);

CREATE TABLE Accesos (
    id_acceso INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    objeto VARCHAR(100), 
    id_permiso INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_permiso) REFERENCES Permisos(id_permiso) ON DELETE CASCADE
);

-- modificacion - rubrica ******************

CREATE TABLE rubricas (
    id_rubrica INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    area_conocimiento VARCHAR(255) NOT NULL, 
    descripcion TEXT,
    fecha_creacion DATE NOT NULL
);

CREATE TABLE criterios (
    id_criterio INT AUTO_INCREMENT PRIMARY KEY,
    id_rubrica INT,
    id_criterio_padre INT NULL, 
    nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT,
    ponderacion DECIMAL(5,2),
    FOREIGN KEY (id_rubrica) REFERENCES rubricas(id_rubrica) ON DELETE CASCADE,
    FOREIGN KEY (id_criterio_padre) REFERENCES criterios(id_criterio) ON DELETE CASCADE
);

CREATE TABLE evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_rubrica INT,
    nocontrol CHAR(10),
    fecha_evaluacion DATE NOT NULL,
    comentarios TEXT,
    FOREIGN KEY (id_rubrica) REFERENCES rubricas(id_rubrica) ON DELETE CASCADE,
    FOREIGN KEY (nocontrol) REFERENCES alumno(nocontrol) ON DELETE CASCADE
);

CREATE TABLE detalles_evaluacion (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_evaluacion INT,
    id_criterio INT,
    calificacion DECIMAL(5,2), 
    FOREIGN KEY (id_evaluacion) REFERENCES evaluaciones(id_evaluacion) ON DELETE CASCADE,
    FOREIGN KEY (id_criterio) REFERENCES criterios(id_criterio) ON DELETE CASCADE
);





