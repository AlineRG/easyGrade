from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "USER"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Contacto(db.Model):
    __tablename__ = "CONTACTO"
    id = db.Column(db.Integer, primary_key=True)
    telefono = db.Column(db.String(30), unique=True, nullable=False)
    direccion = db.Column(db.String(30), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
