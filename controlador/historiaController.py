from app import app
from app import *
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from pdf2image import convert_from_bytes
from pdf2image.exceptions import *
from typing import Container
import os
import base64
import socket
import cv2
import img2pdf
from PIL import Image
from shutil import rmtree
from modelo.personas import *
from modelo.pacientes import *
from modelo.consultas import *


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

    data = process_document(project_id,location ,processor_id,file_path)
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

                f = request.files['Filename']
                filename = secure_filename(f.filename)
                extension = filename.rsplit('.',1)[1].lower()
                nuevoNombre = str(todo.num_doc) + "." + extension
                f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", nuevoNombre))
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
                f = request.files['Filename']
                filename = secure_filename(f.filename)
                extension =filename.rsplit('.',1)[1].lower()
                nuevoNombre =str(doc)+"."+ extension
                f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", nuevoNombre))

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

@app.route('/convertirArchivo',methods=['POST'])
def convertirArchivo():
    outputDir = "/static/archivos/imagenes"
    estado = False
    datos = None
    nomArchiv = request.form['nombreArchivo']
    try:
        if not os.path.isdir(outputDir):
            os.mkdir(outputDir)

        images = convert_from_bytes(open(r'static/archivos/historiasClinicas/'+nomArchiv+'.pdf','rb').read())
        counter = 1

        for i, image in enumerate(images):
            fname = "static/archivos/imagenes/"+nomArchiv+"-"+ str(counter) + ".png"
            counter+=1
            image.save(fname, "PNG")

        datos= None
        estado = True
        mensaje = "Convertido correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


@app.route('/convertirEscalaGrises',methods=['POST'])
def convertirEscalaGrises():
    estado = False
    datos = None
    nomArchiv = request.form['nombreArchivo']

    try:
        counter = 1
        while counter<=2:
            #lecturaDeImagen
            ruta = 'static/archivos/imagenes/'+str(nomArchiv)+'-'+str(counter)+'.png'
            imagen = cv2.imread(ruta,0)
            cv2.imwrite(ruta,imagen)
            counter+=1

        datos= None
        estado = True
        mensaje = "Convertido a Escala de Grises correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


@app.route('/convertirImagen', methods=['POST'])
def convertirImagen():
    estado = False
    datos = None
    nomArchiv = request.form['nombreArchivo']

    try:

        image1 = Image.open(r'static/archivos/imagenes/'+nomArchiv+'-1.png')
        image2 = Image.open(r'static/archivos/imagenes/'+nomArchiv+'-2.png')

        im1 = image1.convert('RGB')
        im2 = image2.convert('RGB')

        imagelist = [im2]

        im1.save(r'static/archivos/historiasClinicas/'+nomArchiv+'.pdf',save_all=True, append_images=imagelist)

        datos= None
        estado = True
        mensaje = "Convertido a pdf correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})
