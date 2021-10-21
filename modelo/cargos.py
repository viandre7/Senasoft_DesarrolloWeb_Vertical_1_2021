from app import db

class Cargo(db.Model):
    __tablename__ = 'cargos' #Nombre de la tabla
    id_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_cargo = db.Column(db.String(45),nullable=False)