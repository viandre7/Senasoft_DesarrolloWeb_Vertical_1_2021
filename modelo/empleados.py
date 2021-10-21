from app import db

class Empleado(db.Model):
    __tablename__ = 'empleados' #Nombre de la tabla
    id_empleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id_cargo'), nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('personas.id_persona'), nullable=False)
    # Necesarios para la relación
    cargo = db.relationship("Cargo",backref=db.backref('cargos',lazy=True))
    persona = db.relationship("Persona",backref=db.backref('personas',lazy=True))
