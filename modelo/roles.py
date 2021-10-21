from app import db

class Rol(db.Model):
    __tablename__ = 'roles' #Nombre de la tabla
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_rol = db.Column(db.String(20),nullable=False)