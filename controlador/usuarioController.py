from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from modelo.personas import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc



@app.route("/iniciarSesion",methods=['POST'])
def iniciarSesion():
    login = request.form['txtUsuario']
    password=request.form['txtClave']
    print(login + password)
    if(login and password):
        print("entroooo al iff")
        try:
            print("aquii")
            usuario = Usuario.query.filter(Usuario.user_name==login).\
                      filter(Usuario.contrasena==password).first()
            print("aqui usuario",usuario)
            if(usuario!=None):
                #se crea la variable de sesión
                session['user']=login
                print('Se inicio sesion')
                return render_template("user/inicioUsuario.html")
            else:
                mensaje="Credenciales de ingreso no validas"
        except exc.SQLAlchemyError as ex:
            mensaje = str(ex)
    else:
        mensaje="Faltan datos"
    return render_template("frmIniciarSesion.html",mensaje=mensaje)




