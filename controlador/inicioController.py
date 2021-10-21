from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc



@app.route('/')
def inicio():
    return render_template('frmIniciarSesion.html')

@app.route('/registrarse')
def acercaDeNosotros():
    return render_template('frmRegistrarse.html')

@app.route('/inicioUsuario')
def consultarSolicitud():
    if("user" in session):
        return render_template('user/inicioUsuario.html')
    else:
        return render_template('frmIniciarSesion.html')


@app.route('/subirHistoria')
def subirHistoria():
    return render_template('user/cargarHistoria.html')

@app.route('/consultarHistoria')
def consultarHistoria():
    return render_template('user/consultarHistoria.html')

@app.route('/mostrarIniciarSesion')
def mostrarIniciarSesion():
    return render_template('frmIniciarSesion.html')
