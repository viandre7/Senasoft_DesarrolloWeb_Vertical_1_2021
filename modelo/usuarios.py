from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios' #Nombre de la tabla
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id_empleado'), nullable=False)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable=False)
    user_name = db.Column(db.String(12), nullable=False, unique=True)
    contrasena = db.Column(db.String(20), nullable=False)
    # Necesarios para la relaicion
    empleado = db.relationship("Empleado",backref=db.backref('empleados',lazy=True))
    rol = db.relationship("Rol",backref=db.backref('roles',lazy=True))

    def __repr__(self):
        return f'{self.user_name},{self.contrasena}'