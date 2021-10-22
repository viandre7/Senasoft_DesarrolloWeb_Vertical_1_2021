from app import app
from modelo.usuarios import *
from modelo.roles import *
from modelo.empleados import *
from modelo.cargos import *
from modelo.consultas import *
from modelo.pacientes import *
from modelo.personas import *
from datetime import datetime
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.utils import secure_filename




# Listar Pedidos
# @app.route('/listarInformacion', methods=['POST'])
# def listarInformacion():
#     estado = False
#     datos = None
#     try:
#         pedidos = Pedido.query.all()
#         if(pedidos !=None):
#             lista=[]
#             for p in pedidos:
#                 fechaPedido = p.pedFechaHora
#                 nuevaFechaPedido = fechaPedido.strftime("%Y-%m-%d") 
#                 pedido=(p.idPedido, p.pedCantidad, nuevaFechaPedido, p.cliente.cliNombre, p.pizza.pizNombre, p.pedEstado)
#                 lista.append(pedido)
#             datos=lista
#             print(lista)
#             estado=True
#             mensaje='Lista de pedidos'
#         else:
#             mensaje='No hay pedidos en el momento'
#     except exc.SQLAlchemyError as ex:
#         mensaje = str(ex)
#     return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})



@app.route("/listarInformacion2",methods=['POST','GET'])
def listarInformacion():

    datos=None
    estado=False
    # codigo = request.form['txtCodigo']
    # print(codigo)
    try:
        informacion = Consulta.query.join(Paciente).join(Persona).first()
        print(informacion)
        print('___________________')
        if(informacion!=None):
            fechaConsulta = informacion.fecha_consulta
            nuevaFechaConsulta = fechaConsulta.strftime("%Y-%m-%d") 
            datos=(informacion.paciente.persona.num_doc,informacion.paciente.persona.nombres, informacion.paciente.persona.apellidos, nuevaFechaConsulta)
            estado=True
            mensaje="Datos del consulta por codigo"
            print(datos)
        else:
            mensaje="No existe consulta por el codigo diligenciado"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    
    # infoRes = ResSolicitud.query.all()
    # print(infoRes)
    return jsonify({"estado":estado, "datos":datos, "mensaje":mensaje})
