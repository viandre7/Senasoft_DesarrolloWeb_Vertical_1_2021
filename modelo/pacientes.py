from app import db
from datetime import datetime

class Paciente(db.Model):
    __tablename__ = 'pacientes' #Nombre de la tabla
    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_persona = db.Column(db.Integer, db.ForeignKey('personas.id_persona'), nullable=False)
    fecha_nacim = db.Column(db.String(20), nullable = False)
    genero = db.Column(db.String(1), nullable=False)
    ocupacion = db.Column(db.String(45), nullable=False)
    estad_civil = db.Column(db.String(12), nullable=False)
    nacionalidad = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)

    # Necesarios para la relación
    person = db.relationship("Persona",backref=db.backref('persona',lazy=True))

    def __repr__(self):
        return f'{self.id_paciente}'
