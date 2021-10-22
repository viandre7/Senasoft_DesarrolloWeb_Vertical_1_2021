from app import db

class Consulta(db.Model):
    __tablename__ = 'consultas' #Nombre de la tabla
    id_consulta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id_empleado'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable=False)
    fecha_consulta = db.Column(db.String(20), nullable=False)
    num_histo = db.Column(db.String(20), nullable=False, unique=True)
    motiv_consu = db.Column(db.String(100), nullable=False)
    detal_consu = db.Column(db.String(200), nullable=False)
    antec_hered_famil = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.String(10), nullable=False)
    tensi_arter = db.Column(db.String(30), nullable=False)
    frecu_respi = db.Column(db.String(30), nullable=False)
    frecu_cardi = db.Column(db.String(30), nullable=False)
    talla = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.String(10), nullable=False)
    imc = db.Column(db.String(10), nullable=False)
    # Necesarios para la relaicion
    empleado = db.relationship("Empleado",backref=db.backref('empleado',lazy=True))
    paciente = db.relationship("Paciente",backref=db.backref('paciente',lazy=True))
