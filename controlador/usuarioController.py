from app import app


from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


@app.route("/iniciarSesion",methods=['POST'])
def iniciarSesion():
    
    return render_template("user/inicioUsuario.html")
