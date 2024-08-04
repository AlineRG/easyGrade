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
