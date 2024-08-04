import sqlite3

conn = sqlite3.connect("myDB.db")
print("Opened database successfully")

conn.execute(
    """CREATE TABLE MAESTROS
         (ID INTEGER PRIMARY KEY NOT NULL,
         NOMBRE VARCHAR NOT NULL,
         APELLIDO VARCHAR NOT NULL,
         TELEFONO VARCHAR,
         DIRECCION VARCHAR,
         CORREO_ELECTRONICO VARCHAR NOT NULL);"""
)
print("Table MAESTROS created successfully")

conn.execute(
    """CREATE TABLE MATERIAS
         (ID INTEGER PRIMARY KEY NOT NULL,
         NOMBRE VARCHAR NOT NULL);"""
)
print("Table MATERIAS created successfully")

conn.execute(
    """CREATE TABLE ALUMNOS
         (ID INTEGER PRIMARY KEY NOT NULL,
         NOMBRE VARCHAR NOT NULL,
         APELLIDO VARCHAR NOT NULL,
         FECHA_NACIMIENTO DATE,
         EMAIL VARCHAR,
         TELEFONO VARCHAR,
         MATERIA_ID INTEGER NOT NULL,
         PASSWORD_ID INTEGER NOT NULL,
         FOREIGN KEY (MATERIA_ID) REFERENCES MATERIAS(ID),
         FOREIGN KEY (PASSWORD_ID) REFERENCES PASSWORD(ID));"""
)
print("Table ALUMNOS created successfully")

conn.execute(
    """CREATE TABLE EJERCICIOS
         (ID INTEGER PRIMARY KEY NOT NULL,
         DESCRIPCION VARCHAR NOT NULL,
         QUESTION VARCHAR NOT NULL,
         ANSWER VARCHAR NOT NULL,
         MATERIA_ID INTEGER NOT NULL,
         FOREIGN KEY (MATERIA_ID) REFERENCES MATERIAS(ID));"""
)
print("Table EJERCICIOS created successfully")
