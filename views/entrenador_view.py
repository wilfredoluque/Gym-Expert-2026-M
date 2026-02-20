from flask import render_template

def list(data):
    return render_template("entrenadores/index.html", data=data)

def create():
    return render_template("entrenadores/create.html")

def edit(item):
    return render_template("entrenadores/edit.html", item=item)
