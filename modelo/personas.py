from app import db

class Persona(db.Model):
    __tablename__ = 'personas' #Nombre de la tabla
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_doc = db.Column(db.Integer,nullable=False, unique=True)
    nombres = db.Column(db.String(30), nullable=False)
    apellidos = db.Column(db.String(30),nullable=False)
    correo = db.Column(db.String(35), nullable=False, unique=True)
    telefono = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f'{self.id_persona}'
