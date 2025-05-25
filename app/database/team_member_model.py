from app.database import db
import uuid

class Jugadores_1(db.Model):
    __tablename__ = "Jugadores-Equipo_1"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(30))
    equipo = db.Column(db.String(15))
    dorsal = db.Column(db.Integer)

class Jugadores_2(db.Model):
    __tablename__ = "Jugadores-Equipo_2"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(30))
    equipo = db.Column(db.Integer)
    dorsal = db.Column(db.Integer)
