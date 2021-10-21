from app import app


from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


from flask import Flask, render_template, session as _session

@app.route('/')
def inicio():
    return render_template('frmIniciarSesion.html')

@app.route('/registrarse')
def acercaDeNosotros():
    return render_template('frmRegistrarse.html')

@app.route('/inicioUsuario')
def consultarSolicitud():
    return render_template('user/inicioUsuario.html')

@app.route('/subirHistoria')
def subirHistoria():
    return render_template('user/cargarHistoria.html')

@app.route('/mostrarIniciarSesion')
def mostrarIniciarSesion():
    return render_template('frmIniciarSesion.html')
