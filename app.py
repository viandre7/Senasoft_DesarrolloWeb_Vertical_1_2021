import os
import json
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


# Crear un objeto de tipo Flask
app = Flask(__name__)

app.secret_key = os.urandom(32) #Es necesario para poder crear variables de sesion

#Cadena de conexcion a la db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/senasoft_2021'
db = SQLAlchemy(app)

#configurar la carpeta donde se van a subir las fotos de las pizzas
app.config['UPLOAD_FOLDER']= './static/archivos'

#Lllamado a los controladores
from keyword import *

from controlador.documento import *
from controlador.usuarioController import *
from controlador.inicioController import *
from controlador.historiaController import *
from controlador.empleadoController import *


# Iniciar la aplicacion
if __name__ == "__main__":
    app.run(port=3000, debug=True)
