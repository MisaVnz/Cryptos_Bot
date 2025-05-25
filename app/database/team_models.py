from app.database import db
import uuid

class Equipos(db.Model):
    __tablename__ = "Equipos"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(50))