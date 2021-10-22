import os
from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from modelo.personas import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.utils import secure_filename




   
@app.route('/agregarEmpleado', methods=['POST'])
def agregarEmpleado():
    """[summary]
    Funcion que agrega datos para crear persona, empleado y usuario 
    en la base de datos

    Returns:
        [json]: [Retorna un objeto json con  3 atributos]
    """
    correo = request.form['txtCorreo']
    cedula = request.form['txtCedula']
    nombre = request.form['txtNombre']
    apellido = request.form['txtApellido']
    celular = request.form['txtCelular']
    cargo = request.form['txtCargo']
    password = request.form['txtPassword']
    estado = False
    datos = None
    print(correo, cedula, nombre, apellido, celular, password, cargo)
    if(correo and cedula and nombre and apellido and celular and cargo and password):
        try:
            print('funciono')
            persona=Persona(num_doc=cedula, nombres=nombre, apellidos=apellido, correo=correo, telefono=celular)
            db.session.add(persona)
            db.session.commit()

            empleado = Empleado(id_cargo=cargo, id_persona=persona.id_persona)
            db.session.add(empleado)
            db.session.commit()
            
            usuario= Usuario(id_empleado=empleado.id_empleado, id_rol=1, user_name=cedula, contrasena=password)
            db.session.add(usuario)
            db.session.commit()

            f = request.files['txtImagen']
            print(f)
            filename = secure_filename(f.filename)
            extension =filename.rsplit('.',1)[1].lower()
            nuevoNombre = str(persona.num_doc) + "." + extension
            f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/firmas", nuevoNombre))
            datos= persona.num_doc
            estado=True
            mensaje= 'Empleado agregado exitosamente'
        except exc.SQLAlchemyError as ex:
            db.session.rollback()
            mensaje = str(ex)
    else:
        mensaje= 'Faltan datos'
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})