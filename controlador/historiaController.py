from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from API.documento import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


@app.route('/clinica')
def inicio():
    return render_template('usuario/subirArchivo.html')

@app.route('/subirHistoria',methods=['POST'])
def subirArchivo():
    estado = False
    datos = None
    try:
        f = request.files['txtHistoria']
        print(f)
        filename = secure_filename(f.filename)
        extension =filename.rsplit('.',1)[1].lower()
        num_doc = "1006509459"
        nuevoNombre = num_doc + "." + extension
        f.save(os.path.join(app.config['UPLOAD_FOLDER']+"/historiasClinicas", nuevoNombre))
        datos= num_doc
        estado = True
        mensaje = "Subido correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})
