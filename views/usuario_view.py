from flask import render_template

def list(data):
    return render_template("usuarios/index.html", data=data)

def create():
    return render_template("usuarios/create.html")

def edit(item):
    return render_template("usuarios/edit.html", item=item)
