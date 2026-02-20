from flask import render_template

def list(data):
    return render_template("asistencias/index.html", data=data)

def create(clientes):
    return render_template("asistencias/create.html", clientes=clientes)
