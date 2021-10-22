from app import app
import requests
from app import *
from datetime import datetime
from modelo.personas import *
from modelo.pacientes import *
from modelo.consultas import *
from modelo.usuarios import *
import base64
import socket
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.utils import secure_filename



project_id ='119257377126'
location = 'us' # Format is 'us' or 'eu'
processor_id ='7a7253cb985a49f2' # Create processor in Cloud Console
 # The local file in your current working directory gcloud config set project my-project-document-329520



@app.route('/subirHistoria',methods=['POST'])
def subirArchivo():
    f = request.files['Filename']
    idempleado = request.form['empleado']
    print(idempleado)
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", filename))

    file_path = './static/archivos/historiasClinicas/'+str(filename)

    print(file_path)
    data = process_document(project_id,location ,processor_id,file_path)
    print("aqui la data")
    print(data)

    session["user"]

    for x in data:
        val , r = x
        if(val == "Dirección"):
            direccion = r
        if val == "Nacionalidad":
            nacionalidad = r
        if val == "Nombres":
            nombre = r
        if val == "Apellidos":
            apellido = r
        if val == "Fecha de nacimiento":
            fechaNaci = r
        if val == "Estado civil":
            estadocivil = r
        if val == "Ocupación":
            ocupacion = r
        if val == "N° documento":
            documento = r
        if val == "Teléfono":
            telefono = r
        if val == "Número de historia":
            nhistoria =r
        if val == "Sexo":
            sexo = r
        if val == "Correo":
            correo = r
        if val == "Edad":
            edad = r
        if val == "FECHA":
            fecha = r
        if val == "MOTIVO DE CONSULTA":
            motivoCon = r
        if val == "DETALLES DE LA CONSULTA":
            detalle = r
        if val == "ANTECEDENTES HEREDOFAMILIARES":
            antecedente = r
        if val == "Frecuencia respiratoria":
            respiratoria = r
        if val ==  "Frecuencia cardiaca":
            cardiaca = r
        if val == "Tensión arterial":
            tension = r
        if val == "Temperatura":
            temperatura = r
        if val == "Firma":
            firma = r
        if val == "Talla":
            talla = r
        if val == "Peso":
            peso = r
        if val == "IMC":
            imc = r
    estado = False
    datos = None
    mensaje = ""
    if(documento and nombre and apellido and correo and telefono and direccion and nacionalidad and fechaNaci and
        estadocivil and ocupacion and documento and telefono and nhistoria and sexo and edad and fecha and motivoCon and
        detalle and antecedente and respiratoria and cardiaca and tension and temperatura and firma and talla and
        peso and imc):
        try:
            existe = Persona.query.filter(Persona.num_doc == documento).first()
            id = str(existe)
            todo = Persona.query.filter(Persona.id_persona == id).first()
            idpa = str(todo)
            aqui = Paciente.query.filter(Paciente.id_persona == idpa).first()

            print(todo.num_doc)
            if existe != None:
                consulta = Consulta()
                consulta.id_empleado = int(idempleado)
                consulta.id_paciente = aqui.id_paciente
                consulta.fecha_consulta = fecha
                consulta.num_histo = nhistoria
                consulta.motiv_consu = motivoCon
                consulta.detal_consu = detalle
                consulta.antec_hered_famil = antecedente
                consulta.temperatura = temperatura
                consulta.tensi_arter = tension
                consulta.frecu_respi = respiratoria
                consulta.frecu_cardi = cardiaca
                consulta.talla = talla
                consulta.peso = peso
                consulta.imc = imc
                db.session.add(consulta)
                db.session.commit()


                pri = request.files['Filename']
                f = secure_filename(pri.filename)
                extension =filename.rsplit('.',1)[1].lower()
                nuevoNombre = str(todo.num_doc) + "." + extension
                pri.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", nuevoNombre))
            else:
                persona = Persona()
                persona.num_doc = documento
                persona.nombres = nombre
                persona.apellidos = apellido
                persona.correo = correo
                persona.telefono = telefono
                db.session.add(persona)
                db.session.commit()
                doc = persona.num_doc

                #aqui se edita el documento y se renombra
                dos = request.files['Filename']
                f = secure_filename(dos.filename)
                extension =filename.rsplit('.',1)[1].lower()
                nuevoNombre = str(doc) + "." + extension
                f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", f))

                #aqui se recoje la id de persona
                id_per = persona.id_persona
                #se realiza la creacion para guadar datos paci
                paciente = Paciente()
                paciente.id_persona = id_per
                paciente.fecha_nacim = fechaNaci
                paciente.genero = sexo
                paciente.ocupacion = ocupacion
                paciente.estad_civil = estadocivil
                paciente.nacionalidad = nacionalidad
                paciente.direccion = direccion
                db.session.add(paciente)
                db.session.commit()
                #aqui se recoje la id de paciente
                id_paci = paciente.id_paciente
                #se realiza la creacion para guadar datos paci
                consulta = Consulta()
                consulta.id_empleado = int(idempleado)
                consulta.id_paciente = id_paci
                consulta.fecha_consulta = fecha
                consulta.num_histo = nhistoria
                consulta.motiv_consu = motivoCon
                consulta.detal_consu = detalle
                consulta.antec_hered_famil = antecedente
                consulta.temperatura = temperatura
                consulta.tensi_arter = tension
                consulta.frecu_respi = respiratoria
                consulta.frecu_cardi = cardiaca
                consulta.talla = talla
                consulta.peso = peso
                consulta.imc = imc
                db.session.add(consulta)
                db.session.commit()

                estado = True
                mensaje = "Datos del paciente creado correctamente"
        except exc.SQLAlchemyError as ex:
            mensaje = str(ex)
    else:
        mensaje = "Faltan datos"
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})
