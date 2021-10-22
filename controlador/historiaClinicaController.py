from app import app
from flask import Flask, request, render_template,jsonify,session
from werkzeug.utils import secure_filename
from sqlalchemy import exc
import os
from pdf2image import convert_from_bytes
from pdf2image.exceptions import *
import cv2
import img2pdf
from PIL import Image

@app.route('/subirArchivo',methods=['POST'])
def subirArchivo():
    estado = False
    datos = None
    try:
        f = request.files['txtHistoria']
        filename = secure_filename(f.filename)
        extension =filename.rsplit('.',1)[1].lower()
        nomCompl = "1006509459"
        fecha ="21-10-2021"
        nuevoNombre = str(nomCompl)+"_"+fecha+"." + extension
        rutaRaiz = app.config['UPLOAD_FOLDER']+"/historiasClinicas/"
        f.save(os.path.join(rutaRaiz,nuevoNombre))
        datos= [nomCompl,fecha]
        estado = True
        mensaje = "Subido correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


@app.route('/convertirArchivo',methods=['POST'])
def convertirArchivo():
    outputDir = "/static/archivos/imagenes"
    estado = False
    datos = None
    nomCompl = request.form['nomCompl']
    fecha = request.form['fechaConsulta']
    try:
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        
        images = convert_from_bytes(open(r'static/archivos/historiasClinicas/'+nomCompl+'.pdf','rb').read())
        counter = 1
        
        for i, image in enumerate(images):
            fname = "static/archivos/imagenes/"+nomCompl+"-"+ str(counter) + ".png"
            counter+=1
            image.save(fname, "PNG")

        datos= nomCompl
        estado = True
        mensaje = "Convertido correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


@app.route('/convertirEscalaGrises',methods=['POST'])
def convertirEscalaGrises():
    estado = False
    datos = None
    nomCompl = request.form['nomCompl']
    fecha = request.form['fechaConsulta']
    
    try:
        counter = 1
        while counter<=2:
            #lecturaDeImagen
            ruta = 'static/archivos/imagenes/'+str(nomCompl)+'-'+str(counter)+'.png'
            imagen = cv2.imread(ruta,0)
            cv2.imwrite(ruta,imagen)
            counter+=1

        datos= nomCompl
        estado = True
        mensaje = "Convertido a Escala de Grises correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


@app.route('/convertirImagen', methods=['POST'])
def convertirImagen():
    estado = False
    datos = None
    nomCompl = request.form['nomCompl']
    fecha = request.form['fechaConsulta']
    
    try:

        image1 = Image.open(r'static/archivos/imagenes/'+nomCompl+'-1.png')
        image2 = Image.open(r'static/archivos/imagenes/'+nomCompl+'-2.png')
        
        im1 = image1.convert('RGB')
        im2 = image2.convert('RGB')

        imagelist = [im2]

        im1.save(r'static/archivos/historiasClinicas/'+nomCompl+'_'+fecha+'.pdf',save_all=True, append_images=imagelist)
       
        datos= nomCompl
        estado = True
        mensaje = "Convertido a pdf correctamente"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)

    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})


    
    
