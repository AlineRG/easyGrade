import sqlite3
import os

print(os.getcwd(), "------------")

conn = sqlite3.connect("instance/myDB.db")
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

conn.execute(
    """CREATE TABLE PASSWORDS
         (ID INTEGER PRIMARY KEY NOT NULL,
         PASSWORD VARCHAR NOT NULL);"""
)
print("Table PASSWORDS created successfully")

conn.execute(
    """CREATE TABLE TAREAS
         (ID INTEGER PRIMARY KEY NOT NULL,
         DESCRIPCION TEXT NOT NULL,
         MATERIA_ID INTEGER NOT NULL,
         ALUMNO_ID INTEGER NOT NULL,
         MAESTRO_ID INTEGER NOT NULL,
         FOREIGN KEY (MATERIA_ID) REFERENCES MATERIAS(ID),
         FOREIGN KEY (ALUMNO_ID) REFERENCES ALUMNOS(ID),
         FOREIGN KEY (MAESTRO_ID) REFERENCES MAESTROS(ID));"""
)
print("Table TAREAS created successfully")

conn.execute(
    """CREATE TABLE EXAMENES
         (ID INTEGER PRIMARY KEY NOT NULL,
         DESCRIPCION TEXT NOT NULL,
         MATERIA_ID INTEGER NOT NULL,
         ALUMNO_ID INTEGER NOT NULL,
         MAESTRO_ID INTEGER NOT NULL,
         FOREIGN KEY (MATERIA_ID) REFERENCES MATERIAS(ID),
         FOREIGN KEY (ALUMNO_ID) REFERENCES ALUMNOS(ID),
         FOREIGN KEY (MAESTRO_ID) REFERENCES MAESTROS(ID));"""
)
print("Table EXAMENES created successfully")

conn.close()