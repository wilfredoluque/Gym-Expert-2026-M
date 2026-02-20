from flask import render_template

def list(data):
    return render_template("rutina/index.html", data=data)

def create(rutinas, ejercicios):
    return render_template("rutina/create.html", rutinas=rutinas, ejercicios=ejercicios)
