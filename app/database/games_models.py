from app.database import db
import uuid

class Equipo_1(db.Model):
    __tablename__ = "Equipo_1"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))

class Equipo_2(db.Model):
    __tablename__ = "Equipo_2"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))

class Fecha(db.Model):
    __tablename__ = "Fecha"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    fecha = db.Column (db.Date)
    
class Ganador(db.Model): 
    __tablename__ = "Equipo_Ganador"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))

class Perdedor(db.Model): 
    __tablename__ = "Equipo_Perdedor"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))

class Team_1_goals(db.Model):
    __tablename__ = "Goles_equipo_1"  
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.Integer) 

class Team_2_goals(db.Model):
    __tablename__ = "Goles_equipo_2"  
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.Integer)  