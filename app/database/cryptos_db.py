from app.database import db
import uuid

class Moneda(db.Model):
    __tablename__ = "Nombre"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))

class Precio(db.Model):
    __tablename__ = "Precio"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))