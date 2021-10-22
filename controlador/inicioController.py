from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from modelo.pacientes import *
from modelo.personas import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from modelo.consultas import *
from modelo.pacientes import *
from modelo.personas import *



@app.route('/')
def inicio():
    user = Usuario.query.all()
    return render_template('frmIniciarSesion.html')


@app.route('/registrarse')
def registrar():
    """[summary]
    Función que permite renderizar al frmRegistro
    Returns:
        [render_template]: [El formulario al cual va a renderizar]
    """
    cargos = Cargo.query.all()
    return render_template('frmRegistrarse.html', cargo = cargos)


@app.route('/inicioUsuario')
def iniciarSesionUsu():
    """[summary]
    Función que permite renderizar al inicio de usuario si la variable user
    está creada, de lo contrario renderiza de nuevo al formulario
    Returns:
        [render_template]: [El formulario al cual va a renderizar]
    """
    if("user" in session):
        return render_template('user/inicioUsuario.html')
    else:
        return render_template('frmIniciarSesion.html')


@app.route('/subirHistoria')
def subirHistoria():
    """[summary]
    Función que permite renderizar al formulario
    cargarHistoria
    Returns:
        [render_template: El formulario al cual va a renderizar]
    """
    if("user" in session):
        return render_template('user/cargarHistoria.html', user = session["idempleado"])
    else:
        return render_template('frmIniciarSesion.html')



@app.route('/consultarHistoria')
def consultarHistoria():
    """[summary]
    Función que permite renderizar al html consultarHistoria
    Returns:
        [render_template: El formulario al cual va a renderizar]
    """
    return render_template('user/consultarHistoria.html')


@app.route('/mostrarIniciarSesion')
def mostrarIniciarSesion():
    """[summary]
    Función que permite renderizar al frmRegistro
    Returns:
        [render_template: El formulario al cual va a renderizar]
    """
    return render_template('frmIniciarSesion.html')

@app.route("/salir")
def salir():
    """[summary]
    Funcion creada para cerraar cesion y limpiar la variable session
    Returns:
        [type]: [description]
    """
    session.clear()
    mensaje="Ha cerrado la sesión"
    return render_template("frmIniciarSesion.html",cerrar=mensaje)
